from ase.build import bulk
from ase.units import Bohr

atoms = bulk('Si', 'diamond', a=5.43 * Bohr)
supercell = atoms.repeat((3, 3, 3))

print(f"Number of atoms: {len(supercell)}")
print(f"Cell volume: {supercell.get_volume():.3f} Bohr^3")
