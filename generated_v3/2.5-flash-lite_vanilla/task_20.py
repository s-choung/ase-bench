from ase.build import nanotube
from ase.calculators.emt import EMT

# Create a (6,6) carbon nanotube with length 4
atoms = nanotube(n=6, m=6, length=4)

# Assign EMT calculator (optional, but good practice for simulation)
atoms.calc = EMT()

# Print the number of atoms
print(f"Number of atoms: {len(atoms)}")

# Print the cell information
print(f"Cell: {atoms.cell}")
