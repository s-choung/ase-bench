from ase.build import bulk
from ase.calculators.emt import EMT
from ase.io import write, read

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

write('POSCAR', atoms, format='vasp')
atoms2 = read('POSCAR', format='vasp')

cell = atoms2.get_cell_lengths_and_angles()
print(len(atoms2))
print(*cell)
