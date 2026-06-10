from ase.build import fcc111, molecule, add_adsorbate

slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)
n2 = molecule('N2')
add_adsorbate(slab, n2, 2.0, position='bridge')

print(len(slab))
print(sorted(set(slab.get_chemical_symbols())))
