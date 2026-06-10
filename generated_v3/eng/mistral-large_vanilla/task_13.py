from ase.lattice.cubic import Diamond
from ase.build import make_supercell

si = Diamond(size=(1, 1, 1), symbol='Si', pbc=True, latticeconstant=5.43)
supercell = make_supercell(si, [[3, 0, 0], [0, 3, 0], [0, 0, 3]])

print(f"Number of atoms: {len(supercell)}")
print(f"Cell volume: {supercell.get_volume():.2f} Å³")
