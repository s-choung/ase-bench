from ase.build import bulk
from ase.io import write, read

write('POSCAR', bulk('Cu', 'fcc', a=3.61))
atoms = read('POSCAR')

print(len(atoms))
print(atoms.cell.cellpar())
