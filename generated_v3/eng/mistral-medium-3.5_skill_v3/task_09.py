from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.io import read, write

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
write('POSCAR', atoms, format='vasp')
atoms_read = read('POSCAR', format='vasp')
print(len(atoms_read), atoms_read.get_cell_lengths_and_angles())
