from ase.build import nanotube
from ase import Atoms

# Create (6,6) carbon nanotube
cnt = nanotube(6, 6, length=4)

# Print information
print(f"Number of atoms: {len(cnt)}")
print(f"Cell: {cnt.cell.array}")
print(f"Periodic boundary conditions: {cnt.pbc}")
