from ase.build import bulk
from ase import Atoms

si_bulk = bulk('Si', 'diamond', a=5.43, cubic=True)
supercell = si_bulk * (3, 3, 3)
print(f"Number of atoms: {len(supercell)}")
print(f"Cell volume: {supercell.get_volume():.3f} Å³")
