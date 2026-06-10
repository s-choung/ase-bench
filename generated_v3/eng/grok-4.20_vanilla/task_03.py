from ase.build import mx2
from ase.io import write

atoms = mx2(formula='MoS2', kind='2H', a=3.18, thickness=3.17)
atoms.center(vacuum=10.0, axis=2)

print(atoms.cell)

write('MoS2.vasp', atoms, vasp5=True, sort=True)
