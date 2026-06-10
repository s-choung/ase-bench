from ase.build import bcc110
from ase import Atoms

# Fe BCC(110) surface: 4 layers of atoms + 10 Å vacuum in the z‑direction
slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

# Ensure periodicity only in the plane (add FixBase Atoms tags)
for i in range(slab.size):
    slab.atoms[i].tag = i
slab.set_constraint('Fe', tag=0)   # top vacuum layer marked with tag 0

# Attach built‑in EMT calculator
from ase.calculators.emt import EMT
slab.calc = EMT()

print('Number of atoms:', slab.get_number_of_atoms())
print('Cell dimensions:')
print('a, b:', slab.get_cell_lengths_and_angles()[:3])   # a, b, c
print('c:', slab.get_cell_lengths_and_angles()[3])
