import ase
from ase.lattice.cubic import NaCl
from ase.io import write, read

atoms = NaCl(a=5.64)
write('NaCl.cif', atoms)
atoms_read = read('NaCl.cif')
print("Spacegroup:", atoms_read.get_spacegroup())
print("Number of atoms:", len(atoms_read))
