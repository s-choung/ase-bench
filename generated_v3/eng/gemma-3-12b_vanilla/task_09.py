from ase.build import fcc
from ase.io import write, read
from ase.calculators.emt import EMT
from ase.lattice.cubic import Cubic

a = 3.61
atoms = fcc('Cu', a=a)
atoms.calc = EMT()

write('Cu_fcc.vasp', atoms, format='vasp')

atoms_read = read('Cu_fcc.vasp')

print(len(atoms_read))
print(atoms_read.get_cell())
