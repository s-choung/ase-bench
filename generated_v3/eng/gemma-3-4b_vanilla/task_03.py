from ase import Atoms
from ase.build import monolayer
from ase.calculators import EMT, LJ

slab = monolayer('MoS2', size=(4, 4), analyzer='relaxed')
slab.calc = EMT()
slab.calc.kpts = (2, 2, 1)
slab.add_atoms(Atoms({ 'Mo': [0, 0, 0], 'S': [1, 1, 0], 'S': [2, 2, 0] }))
slab.calc = LJ()
slab.add_atoms(Atoms({ 'Mo': [0, 0, 0], 'S': [1, 1, 0], 'S': [2, 2, 0] }))
slab.vacuum = 10.0
print(slab.cell)
