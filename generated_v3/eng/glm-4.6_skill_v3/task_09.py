from ase.build import bulk
from ase.io import write, read

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True)
write('POSCAR', atoms, format='vasp')

atoms_read = read('POSCAR', format='vasp')
print(f"Number of atoms: {len(atoms_read)}")
print(f"Cell parameters: {atoms_read.get_cell_lengths_and_angles()}")
