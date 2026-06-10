from ase.build import bulk
from ase.io import read, write
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()
write('POSCAR', atoms, format='vasp')
atoms = read('POSCAR', format='vasp')
print(len(atoms))
print(atoms.get_cell_lengths_and_angles())
