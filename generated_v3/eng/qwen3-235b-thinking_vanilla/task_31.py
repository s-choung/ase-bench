from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.units import GPa

atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
print("Initial volume:", atoms.get_cell().volume)
atoms.calc = EMT()
dyn = NPTBerendsen(atoms, 1.0, 500, 10 * GPa, ttime=100.0, pfactor=1e2)
dyn.run(100)
print("Final volume:", atoms.get_cell().volume)
