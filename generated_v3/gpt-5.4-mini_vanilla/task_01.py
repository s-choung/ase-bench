from ase.build import bulk
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc', a=3.615)
supercell = atoms.repeat((2, 2, 2))
supercell.calc = EMT()

print("Cell:")
print(supercell.cell)
print("Number of atoms:", len(supercell))
