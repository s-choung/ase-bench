from ase import Atoms
from ase.io import write, read
from ase.lattice.cubic import FaceCenteredCubic

au_bulk = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], symbol='Au', size=(1, 1, 1))
write('au_bulk.xyz', au_bulk)
au_loaded = read('au_bulk.xyz')

for atom in au_loaded:
    print(f"{atom.symbol} {atom.position}")
