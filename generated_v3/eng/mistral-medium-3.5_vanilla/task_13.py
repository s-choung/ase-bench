from ase.lattice.cubic import Diamond
from ase.build import make_supercell

si = Diamond('Si', latticeconstant=5.43)
supercell = make_supercell(si, [[3, 0, 0], [0, 3, 0], [0, 0, 3]])
print(f"Atoms: {len(supercell)}, Volume: {supercell.get_volume():.2f} Å³")
