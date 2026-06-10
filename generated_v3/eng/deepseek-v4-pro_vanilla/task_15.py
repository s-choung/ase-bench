from ase.build import fcc100

# Create Cu(100) slab with 3 layers, (3,3,3) in-plane repetition, 12 Å vacuum
slab = fcc100('Cu', size=(3, 3, 3), a=3.61, vacuum=12)

# Print number of atoms and cell information
print('Number of atoms:', len(slab))
print('Cell info:')
print(slab.cell)
