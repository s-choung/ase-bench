from ase.build import surface, add_vacuum, bulk

# Reference Cu bulk
cu = bulk('Cu', 'fcc', a=3.61)

# Create (2,1,1) surface with 3 atomic layers
slab = surface(cu, (2, 1, 1), layers=3)

# Add 10 Å of vacuum
add_vacuum(slab, 10.0)

print('Number of atoms:', len(slab))
print('Cell:')
print(slab.get_cell())
