from ase import Atoms, io
from ase.lattice.cubic import FaceCenteredCubic

au = FaceCenteredCubic(symbol='Au', latticeconstant=4.08)
au.write('au.xyz')

atoms = io.read('au.xyz')
print([atom.symbol for atom in atoms])
print(atoms.positions)
