from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Create Cu bulk with EMT calculator
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Optimize the structure
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms)
vib.run()

# Get vibrational energies
vib_energies = vib.get_energies()

# Calculate Helmholtz free energy at 300K
thermo = HarmonicThermo(vib_energies=vib_energies, potentialenergy=atoms.get_potential_energy())
F = thermo.get_helmholtz_energy(temperature=300)

print(f"Helmholtz free energy at 300K: {F:.4f} eV")

# Clean vibration files
vib.clean()
