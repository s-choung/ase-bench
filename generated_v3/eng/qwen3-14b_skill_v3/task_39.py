from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc')
write('au_fcc.xyz', atoms)
atoms_read = read('au_fcc.xyz')
print("Atom types:", atoms_read.get_chemical_symbols())
print("Positions:\n", atoms_read.get_positions())
