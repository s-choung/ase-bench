from ase.build import bulk
from ase import Atoms
from ase.io import write

atoms = bulk('Cu', 'fcc', a=3.6)
supercell = atoms.repeat((2, 2, 2))

print(supercell.get_cell_lengths_and_angles())
print(len(supercell.get_positions()))
