from ase.build import bulk
from ase.io import write, read

atoms = bulk('Cu', 'fcc')
write('POSCAR', atoms, format='vasp')

atoms_read = read('POSCAR')
print(f"Number of atoms: {len(atoms_read)}")
print(f"Cell parameters: {atoms_read.cell.cellpar()}")
