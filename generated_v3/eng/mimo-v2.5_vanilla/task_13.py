from ase import Atoms
from ase.lattice import bulk

# Create Si diamond structure and repeat to 3x3x3 supercell
si = bulk('Si', 'diamond', a=5.43, cubic=True)
si = si.repeat((3, 3, 3))

print(f"Number of atoms: {len(si)}")
print(f"Cell volume: {si.get_volume():.2f} Å³")
