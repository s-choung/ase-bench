from ase.build import fcc100
from ase import units

# Cu(100) slab: 3 layers, 3x3 in‑plane supercell, 12 Å vacuum
slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)

# Output
print("Number of atoms :", slab.get_number_of_atoms())
print("Cell (a, b, c, α, β, γ) :", slab.get_cell_lengths_and_angles())
