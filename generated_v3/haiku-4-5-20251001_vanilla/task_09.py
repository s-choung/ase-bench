from ase.build import bulk
from ase.io import read, write

cu = bulk('Cu', 'fcc', a=3.61)
write('POSCAR', cu, format='vasp')

atoms = read('POSCAR')
print(f"Number of atoms: {len(atoms)}")
print(f"Cell parameters:\n{atoms.cell}")
