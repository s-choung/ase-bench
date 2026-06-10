from ase.build import bulk
from ase.calculators.emt import EMT

supercell = bulk('Cu', 'fcc').repeat((2, 2, 2))
supercell.calc = EMT()

print("Cell info:")
print(supercell.cell)
print("Number of atoms:", len(supercell))
