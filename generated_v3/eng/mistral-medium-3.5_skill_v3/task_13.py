from ase.build import bulk
from ase.calculators.emt import EMT

atoms = bulk('Si', 'diamond', a=5.43)
atoms = atoms * (3, 3, 3)
atoms.calc = EMT()
print(len(atoms), atoms.get_volume())
