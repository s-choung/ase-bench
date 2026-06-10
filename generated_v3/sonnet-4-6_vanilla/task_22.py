from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

n2 = molecule('N2')

add_adsorbate(slab, n2, height=2.0, position='bridge')

slab.calc = EMT()

print(f"총 원자 수: {len(slab)}")
print(f"원자 종류: {set(slab.get_chemical_symbols())}")
print(f"원자 목록: {slab.get_chemical_symbols()}")
