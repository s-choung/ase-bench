from ase import Atoms
from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
supercell = atoms.repeat((2, 2, inside=True)
print('Original cell info:', atoms.cell)
print('Original number of atoms:', len(atoms))
print('Supercell info:', supercell.cell)
print('Supercell number of atoms:', len(supercell))
