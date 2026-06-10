from ase import Atoms
from ase.build import bulk
from ase.lattice import diamond
from ase.units import Angstrom

atoms = bulk('Si', crystalstructure=diamond, a=5.43)
supercell = atoms * (3, 3, 3)

print(f"Number of atoms: {len(supercell)}")
print(f"Cell volume: {supercell.get_volume()} Angstrom^3")
