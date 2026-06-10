from ase.build import fcc111, add_adsorbate, molecule

slab = fcc111('Pt', size=(1, 1, 4), vacuum=10.0)
add_adsorbate(slab, molecule('CO'), 1.8, 'ontop')
print(len(slab))
