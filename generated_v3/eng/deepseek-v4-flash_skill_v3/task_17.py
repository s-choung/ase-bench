from ase.build import bulk, surface, add_vacuum

# Create Cu bulk with FCC structure
cu = bulk('Cu', 'fcc', a=3.6)

# Cut (2,1,1) surface with 3 layers
slab = surface(cu, (2, 1, 1), layers=3)

# Add 10 Å vacuum in z-direction
add_vacuum(slab, 10.0)

# Print number of atoms and cell
print("Number of atoms:", len(slab))
print("Cell:")
print(slab.cell)
