from ase import Atoms
from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.07)
write('Au_bulk.xyz', atoms)

atoms_read = read('Au_bulk.xyz')

print("Atom types:", [atom.symbol for atom in atoms_read])
print("Atom positions:", atoms_read.positions)
