import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Create bulk Cu and optimize
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms, name='cu_vib')
vib.run()
vib_energies = vib.get_energies()  # eV
vib.summary()
vib.clean()

# Harmonic thermochemistry
thermo = HarmonicThermo(vib_energies=vib_energies,
                       potentialenergy=atoms.get_potential_energy())
F = thermo.get_helmholtz_energy(temperature=300)

print(f"Helmholtz free energy at 300 K: {F:.6f} eV")
