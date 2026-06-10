from ase.build import bulk
from ase.units import Angstrom

si = bulk('Si', 'diamond', a=5.43)
si_super = si.repeat((3, 3, 3))

print("Number of atoms:", len(si_super))
print("Cell volume (Å^3):", si_super.get_volume())
