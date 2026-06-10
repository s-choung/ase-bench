from ase.build import bulk, surface

# Cu bulk with default lattice constant (fcc, a=3.615 Å)
cu = bulk('Cu', 'fcc', a=3.615)

# Create (2,1,1) slab with 3 layers
slab = surface(cu, (2, 1, 1), layers=3)

# Add 10 Å vacuum along the surface normal (z-direction)
slab.center(vacuum=10, axis=2)

# Print number of atoms and cell
print('Number of atoms:', len(slab))
print('Cell:\n', slab.cell)
