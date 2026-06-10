from ase.build import bulk
from ase import units

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)
supercell = atoms * (2, 2, 2)
print(supercell.get_cell_lengths_and_angles())
print(len(supercell))
