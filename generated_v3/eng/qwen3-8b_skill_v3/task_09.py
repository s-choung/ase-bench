from ase.build import bulk
from ase.io import write, read

atoms = bulk('Cu', 'fcc', a=3.6)
write('POSCAR', atoms, format='vasp')
atoms_read = read('POSCAR', format='vasp')

print(f"Number of atoms: {atoms_read.get_number_of_atoms()}")
print("Cell parameters:")
print(atoms_read.get_cell())
