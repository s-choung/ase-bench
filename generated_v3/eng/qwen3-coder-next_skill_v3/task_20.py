from ase import Atoms
from ase.build import nanotube
from ase.io import write

# Create (6,6) carbon nanotube with length=4
cnt = nanotube(6, 6, length=4)

# Print number of atoms
print(f"Number of atoms: {len(cnt)}")

# Print cell info
cell = cnt.get_cell()
print(f"Cell vectors (Å):\n{cell}")
print(f"Cell parameters (a, b, c, α, β, γ): {cnt.get_cell_lengths_and_angles()}")
