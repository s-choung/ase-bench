from ase.build import fcc111, molecule, add_adsorbate

slab = fcc111('Al', size=(1, 1, 3), vacuum=10.0)
add_adsorbate(slab, molecule('N2'), 2.0, 'bridge')
print(len(slab))
print(sorted(set(slab.symbols)))
