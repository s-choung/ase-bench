from ase.build import fcc111, molecule, add_adsorbate
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)
n2 = molecule('N2')
add_adsorbate(slab, n2, 2.0, 'bridge')
print(len(slab), set(slab.get_chemical_symbols()))
