import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.thermochemistry import HarmonicThermo
from ase.build import bulk
from ase.optimize import BFGS

# Create Cu bulk
atoms = bulk('Cu','fcc',a=3.5)
atoms.calc = EMT()

# Optimize the cell and positions
BFGS(atoms).run(fmax=0.01)

# Get vibrations
vib = Vibrations(atoms, name='vib')
vib.run()
vib_energies = vib.get_frequencies()

# Calculate Helmholtz free energy at 300K
thermo = HarmonicThermo(vib_energies=vib_energies, atoms=atoms,
                        geometry='linear', symmetrynumber=2, spin=0)
G = thermo.get_helmholtz_energy(temperature=300.0, pressure=1.0)  #unitless pressure

print(f"Helmholtz free energy at 300K: {G} eV")
