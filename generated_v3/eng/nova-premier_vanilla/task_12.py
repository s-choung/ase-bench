from ase import Atoms
from ase.lattice.spacegroup import crystal

a = 2.95
c = 1.59 * a
struct = crystal('HCP', [(a, a, c)], basis=[(0, 0, 0)], spacegroup=194,
                 cellpar=[a, a, c, 90, 90, 120], symbol='Ti')

print(struct.get_cell())
print(struct.get_positions())
