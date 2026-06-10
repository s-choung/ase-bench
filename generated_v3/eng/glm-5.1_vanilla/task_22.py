from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT

slab = fcc111('Al', size=(1, 1, 3), vacuum=10.0)
n2 = molecule('N2')
add_adsorbate(slab, n2, height=2.0, position='bridge')
slab.calc = EMT()

print(f"Number of atoms: {len(slab)}")
print(f"Atom types: {slab.get_chemical_symbols()}")
