from ase.build import bulk, surface, add_vacuum
from ase.cell import Cell
from ase.io import write

# Cu FCC bulk with lattice constant a = 3.615 Å
atoms = bulk('Cu', 'fcc', a=3.615)

# Cut surface perpendicular to Miller index (2,1,1)
slab = surface(atoms, indices=(2,1,1), layers=3)

# Add 10 Å vacuum in z‑direction
slab = add_vacuum(slab, 10.0)

print('Number of atoms:', slab.get_number_of_atoms())
print('Cell:')
for d, _ell in zip(('a','b','c'), slab.get_cell_lengths_and_angles()):
    print(f'  {d}: {d}_length={slab.get_cell_length(d)} Å, angle={d}: {slab.get_angle(d)}°')
