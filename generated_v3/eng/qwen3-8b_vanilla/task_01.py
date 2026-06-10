from ase.build import fcc
from ase import Atoms

bulk = fcc('Cu', size=(1,1,1), a=3.615)
supercell = bulk.repeat((2,2,2))

print("Cell:")
print(supercell.cell)
print("Number of atoms:", len(supercell))
