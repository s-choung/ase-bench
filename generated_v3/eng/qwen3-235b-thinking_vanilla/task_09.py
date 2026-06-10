from ase import bulk
from ase.io import write, read

cu = bulk('Cu', 'fcc', a=3.6, cubic=True)
write('POSCAR', cu)
atoms = read('POSCAR')
print(len(atoms))
print(atoms.get_cell_lengths_and_angles())
