from ase.build import bulk
from ase.calculators.emt import EMT
from ase import units

# Create a bulk with diamond structure and Si as the element
atoms = bulk('Si', a=5.43, crystalstructure='diamond')

# Scales the bulk to make a supercell 3x3x3
atoms = atoms.repeat( (3, 3, 3) )

# Assign EMT calculator
atoms.calculation = EMT()

# Print number of atoms and cell volume
print(f"Number of atoms in the supercell: {len(atoms)}")
print(f"Cell volume: {atoms.get_volume()} Å³")
print(f"Cell volume: {atoms.get_volume() / units.angstrom**3:.2f}")
print(f"Number of atoms: {len(atoms) / (len(atoms.positions) / 3:.2f}")
