from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

n2 = molecule('N2')
n2.set_cell([3.0, 3.0, 3.0])
n2.center(vacuum=1.5)

calc = EMT()
n2.calc = calc

dyn = Vibrations(n2, trajectory='n2.traj')
dyn.run(calculator=calc)

frequencies = dyn.frequencies
print(frequencies)
