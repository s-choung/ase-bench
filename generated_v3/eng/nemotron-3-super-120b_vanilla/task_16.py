from ase.build import bulk, surface

# Create bulk Fe (BCC)
fe_bulk = bulk('Fe', 'bcc', a=2.87)

# Generate Fe(110) slab with 4 layers and 10 Å vacuum
slab = surface(fe_bulk, (1, 1, 0), layers=4, vacuum=10.0)

# Replicate to obtain a 2×2 in‑plane supercell
slab = slab.repeat((2, 2, 1))

# Output requested information
print("Number of atoms:", slab.get_number_of_atoms())
print("Cell:\n", slab.get_cell())
