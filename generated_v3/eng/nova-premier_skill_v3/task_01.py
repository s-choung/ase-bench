from ase import Atoms
from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.6)
atoms *= (2,2,2)

print("Cell lengths/angles:", atoms.get_cell_lengths_and_angles())
print("Atom count:", len(atoms))
