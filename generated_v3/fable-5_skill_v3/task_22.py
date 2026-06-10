from ase.build import fcc111, molecule, add_adsorbate

slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)
n2 = molecule('N2')
add_adsorbate(slab, n2, height=2.0, position='bridge')

print("원자 수:", len(slab))
print("원자 종류:", set(slab.get_chemical_symbols()))
print("화학식:", slab.get_chemical_formula())
