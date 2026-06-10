from ase.spacegroup import crystal
from ase.io import write, read

# Create NaCl crystal structure
atoms_NaCl = crystal(symbols=['Na', 'Cl'], basis=[(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup=225)
write('NaCl.cif', atoms_NaCl, format='cif')

# Read the CIF file back
atoms_read = read('NaCl.cif')

# Print spacegroup information
print("Spacegroup:", atoms_read.get_spacegroup())
print("Number of atoms:", len(atoms_read))
