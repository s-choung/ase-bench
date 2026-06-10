from ase import Atoms

# Create Cu FCC bulk
atoms = Atoms('Cu', basis='fcc', a=3.6, pbc=True, cell='fcc', kpts=[3, 3, 3])

# Write to VASP POSCAR format
write('Cu_POSCAR', atoms, format='vasp')

# Read back the POSCAR file
atoms_read = Atoms('Cu_POSCAR', format='vasp')

# Print the number of atoms
print("Number of atoms:", len(atoms_read))

# Print the cell parameters
cell = atoms_read.get_cell()
print("Cell parameters:", cell)
