from ase.build import surface

slab = surface('Fe', (1, 1, 0), (2, 2, 4), a=2.87, vacuum=10.0)

print(f'Number of atoms: {len(slab)}')
print(f'Cell size:\n{slab.cell}')
