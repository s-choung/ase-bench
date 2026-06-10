from ase.build import bulk
from ase.io import write, read

# Cu FCC bulk (default lattice constant ~3.6 Å)
atoms = bulk('Cu', 'fcc', a=3.6)

# Save as VASP POSCAR
write('POSCAR', atoms, format='vasp')

# Read it back
atoms_back = read('POSCAR')

# Output
print(atoms_back.get_number_of_atoms())
print(atoms_back.get_cell())
