from ase.build import mx2
from ase.calculators.emt import EMT

atoms = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=10)
atoms.calc = EMT()
print(atoms.cell)
