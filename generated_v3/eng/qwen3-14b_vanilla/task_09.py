from ase.build import bulk
from ase.io import write, read

atoms = bulk('Cu', 'fcc', a=3.6)
write('POSCAR', atoms)
atoms_read = read('POSCAR')
print(len(atoms_read))
print(atoms_read.cell.lengths())
