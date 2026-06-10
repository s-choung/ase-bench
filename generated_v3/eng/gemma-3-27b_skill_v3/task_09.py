from ase import Atoms
from ase.build import bulk
from ase.io import write, read

atoms = bulk('Cu', 'fcc', a=3.6)
write('POSCAR', atoms, format='vasp')
atoms_read = read('POSCAR', format='vasp')

print(f"Number of atoms: {len(atoms_read)}")
cell_lengths_and_angles = atoms_read.get_cell_lengths_and_angles()
print(f"Cell parameters (a, b, c, alpha, beta, gamma): {cell_lengths_and_angles}")
