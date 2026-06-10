from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()
write('au_fcc.xyz', atoms)

atoms_read = read('au_fcc.xyz', index=0)
print('Atom types:', atoms_read.get_chemical_symbols())
print('Positions:\n', atoms_read.get_positions())
