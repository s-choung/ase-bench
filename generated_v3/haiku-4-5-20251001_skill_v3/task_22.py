from ase.build import fcc111, molecule, add_adsorbate
from ase.io import write

slab = fcc111('Al', size=(3, 3, 3), vacuum=10.0)
n2 = molecule('N2')
add_adsorbate(slab, n2, height=2.0, position='bridge')

print(f"Total atoms: {len(slab)}")
print(f"Atom types: {slab.get_chemical_symbols()}")
print(f"Al: {slab.get_chemical_symbols().count('Al')}, N: {slab.get_chemical_symbols().count('N')}")

write('al111_n2_bridge.xyz', slab)
