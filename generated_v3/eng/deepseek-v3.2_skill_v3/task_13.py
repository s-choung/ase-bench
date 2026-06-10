from ase.build import bulk
from ase import Atoms

atoms = bulk('Si', 'diamond', a=5.43)
supercell = atoms * (3, 3, 3)

print(f"Number of atoms: {len(supercell)}")
print(f"Cell volume: {supercell.get_volume():.2f} Å³")
