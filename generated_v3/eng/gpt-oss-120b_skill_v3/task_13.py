from ase.build import bulk
from ase import units

# bulk Si, diamond (cubic) with a = 5.43 Å
si = bulk('Si', 'diamond', a=5.43)

# 3×3×3 supercell
si_sc = si.repeat((3, 3, 3))

print('Number of atoms:', len(si_sc))
print('Cell volume (Å³):', si_sc.get_volume())
