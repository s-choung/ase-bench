from ase import Atoms
from ase.calculators.emt import EMT
from ase.geometry.treatments import Noshells

Au = Atoms.from_pqr('Au.pqr')
Au.cell *= 1.0
Au.center = (0, 0, 0)
Au.calc = EMT()
Au.calc.kpts = (2, 2, 2)
Au.treat = Noshells(Au, noshells=3)
print(len(Au))
print(Au.get_center_of_mass())
