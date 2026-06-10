from ase import Atoms
from ase.build import bulk, make_supercell

# bulk Si (diamond)
si = bulk('Si', 'diamond', a=5.43)

# 3x3x3 supercell
si_super = make_supercell(si, [[3, 0, 0], [0, 3, 0], [0, 0, 3]])

print("Number of atoms:", len(si_super))
print("Cell volume (Å³):", si_super.get_volume())
