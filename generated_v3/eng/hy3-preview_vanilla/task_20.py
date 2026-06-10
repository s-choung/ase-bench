from ase.build import nanotube
from ase.io import write

# Create (6,6) carbon nanotube with length 4 Å
cnt = nanotube(6, 6, length=4)

# Print number of atoms
print(f"Number of atoms: {len(cnt)}")

# Print cell information
print("Cell dimensions (Å):")
print(cnt.cell)
