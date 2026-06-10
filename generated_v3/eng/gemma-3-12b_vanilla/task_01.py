from ase.build import fcc
from ase.calculators.emt import EMT
from ase.io import write

atoms = fcc('Cu', size=(2, 2, 2))
atoms.calc = EMT()
write('Cu_fcc_supercell.xyz', atoms)
print(atoms.cell)
print(len(atoms))
