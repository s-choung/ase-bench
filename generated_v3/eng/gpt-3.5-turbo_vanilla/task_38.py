from ase import Atoms
from ase.calculators.emt import EMT
from ase.thermochemistry import HarmonicThermo

# Create a Cu bulk structure
atoms = Atoms('Cu', positions=[(0, 0, 0)], cell=(3, 3, 3), pbc=True)

# Set up the EMT calculator
atoms.calc = EMT()

# Get the harmonic thermo
thermo = HarmonicThermo(atoms)

# Compute the Helmholtz free energy at 300K in eV
helmholtz_free_energy = thermo.get_helmholtz_energy(temperature=300)
print(helmholtz_free_energy, "eV")
