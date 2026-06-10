from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.05, cubic=True)
write('au_fcc.xyz', atoms)
atoms_read = read('au_fcc.xyz')
print("Atom types:", atoms_read.get_chemical_symbols())
print("Positions:", atoms_read.get_positions())
