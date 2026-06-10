from ase.build import bulk
from ase.io import write, read

cu = bulk('Cu', 'fcc', a=3.615)
write('POSCAR', cu, format='vasp')

atoms = read('POSCAR', format='vasp')
print(f"Number of atoms: {len(atoms)}")
print(f"Cell parameters:\n{atoms.cell}")
print(f"Cell lengths and angles: {atoms.cell.cellpar()}")
