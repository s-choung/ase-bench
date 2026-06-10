from ase import Atoms
from ase.build import add_vacuum

a0 = 3.16  # MoS2 in-plane lattice constant (Å)
d_ms = 1.68  # Mo-S bond length (Å)
cell = [[a0, 0, 0], [a0/2, (a0*3**0.5)/2, 0], [0, 0, 2*d_ms]]
mos2 = Atoms('MoS2', positions=[(0,0,0), (a0/3, (a0*3**0.5)/3, d_ms), (2*a0/3, 2*(a0*3**0.5)/3, -d_ms)], cell=cell, pbc=(True, True, False))
add_vacuum(mos2, 10.0)
print(mos2.get_cell_lengths_and_angles())
