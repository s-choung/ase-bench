from ase.build import bulk
from ase.calculators.emt import EMT

atoms = bulk('Ti', 'hcp', a=2.95, covera=1.59)
atoms.calc = EMT()

print("Cell vectors:")
print(atoms.get_cell())
print("Atomic positions:")
print(atoms.get_positions())
