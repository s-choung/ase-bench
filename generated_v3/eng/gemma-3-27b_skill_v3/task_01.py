from ase import Atoms
from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms.repeat((2, 2, 2))

print(atoms.get_cell_lengths_and_angles())
print(len(atoms))
