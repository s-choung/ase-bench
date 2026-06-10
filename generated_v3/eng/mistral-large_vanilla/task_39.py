from ase.lattice.cubic import FaceCenteredCubic
from ase.io import write, read

bulk = FaceCenteredCubic('Au', size=(2, 2, 2))
write('au_fcc.xyz', bulk)

atoms = read('au_fcc.xyz')
print(atoms.get_chemical_symbols())
print(atoms.positions)
