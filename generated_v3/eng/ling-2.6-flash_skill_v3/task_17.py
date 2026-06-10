from ase import Atoms
from ase.build import surface, add_vacuum

slab: Atoms = surface('Cu', (2, 1, 1), layers=3, vacuum=10)
print(f'Number of atoms: {len(slab)}')
print(f'Cell:\n{slab.get_cell()}')
