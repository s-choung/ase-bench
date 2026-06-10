from ase.build import fcc111, molecule, add_adsorbate, add_vacuum

slab = fcc111('Al', (2, 2, 3), vacuum=10.0)
n2 = molecule('N2')
add_adsorbate(slab, n2, 2.0, 'bridge')
add_vacuum(slab, 10.0)

symbols = slab.get_chemical_symbols()
al = symbols.count('Al')
n = symbols.count('N')

print(f'Number of atoms: {len(symbols)}')
print(f'Al: {al}, N: {n}')
