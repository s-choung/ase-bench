from ase.build import bulk
from ase.calculators.emt import EMT
from ase.io import read, write

atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()

write('au_bulk.xyz', atoms)
atoms_read = read('au_bulk.xyz')

print("Atom types:", atoms_read.get_chemical_symbols())
print("Positions:\n", atoms_read.get_positions())
