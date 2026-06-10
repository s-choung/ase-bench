from ase.build import fcc111, add_adsorbate, molecule
from ase.visualize import view

slab = fcc111('Al', size=(3, 3, 3), vacuum=10.0)
n2 = molecule('N2')
add_adsorbate(slab, n2, height=2.0, position='bridge')

print(f"Number of atoms: {len(slab)}")
print("Atom types:", set(slab.get_chemical_symbols()))
