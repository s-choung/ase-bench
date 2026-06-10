from ase.build import fcc111
from ase.io import write, read

atoms = fcc111('Au', size=(2, 2, 2))
write('Au_fcc.xyz', atoms)
atoms_read = read('Au_fcc.xyz')

print("Atom types:", [atom.symbol for atom in atoms_read])
print("Atom positions:", atoms_read.get_positions())
