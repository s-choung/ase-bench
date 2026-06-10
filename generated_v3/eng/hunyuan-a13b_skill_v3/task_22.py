from ase import Atoms, units
from ase.build import fcc111, add_adsorbate, add_vacuum
from ase.atom import Atom

slab = fcc111('Al', size=(3, 3, 3), vacuum=10.0)
slab.set_cell(slab.cell * (1, 1, 1))  # Ensure cell is set correctly

n2 = molecule('N2', positions=[(0, 0, 0.5)], pbc=False)
add_adsorbate(slab, n2, height=2.0, position='ontop')

final_structure = slab + n2

print("Number of atoms:", len(final_structure))
print("Atom types:", [a.symbol for a in final_structure])
