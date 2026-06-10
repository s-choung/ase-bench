from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
import numpy as np

# Create and optimize Cu bulk
atoms = Atoms('Cu', positions=[(0, 0, 0)], cell=[3.6, 3.6, 3.6], pbc=True)
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Calculate vibrations (need to create a supercell for meaningful vibrations)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Compute vibrational frequencies
vib = Vibrations(atoms, name='vib')
vib.run()
vib_energies = vib.get_energies()  # eV

# Compute Helmholtz free energy at 300K
thermo = HarmonicThermo(vib_energies=vib_energies, atoms=atoms)
F = thermo.get_helmholtz_energy(temperature=300)

print(f"Helmholtz free energy at 300K: {F:.6f} eV")
vib.clean()
