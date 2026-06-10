from ase.build import fcc111, molecule, add_adsorbate
slab = fcc111('Al', (2, 2, 3), vacuum=10.0)
n2 = molecule('N2')
add_adsorbate(slab, n2, 2.0, 'bridge')
print(len(slab), slab.get_chemical_symbols())
