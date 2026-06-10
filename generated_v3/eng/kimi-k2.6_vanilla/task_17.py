from ase.build import bulk, surface
from ase.calculators.emt import EMT

atoms = bulk('Cu', crystalstructure='fcc', a=3.61, cubic=True)
slab = surface(atoms, indices=(2, 1, 1), layers=3, vacuum=10.0)
slab.calc = EMT()

print(len(slab))
print(slab.cell)
