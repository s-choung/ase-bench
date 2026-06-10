from ase.spacegroup import crystal
from ase.io import write, read

atoms = crystal('NaCl', [(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup='Fm-3m', lattice_parameters=5.64)
write('NaCl.cif', atoms)
atoms_read = read('NaCl.cif')
print("Spacegroup:", atoms_read.get_spacegroup())
print("Number of atoms:", len(atoms_read))
