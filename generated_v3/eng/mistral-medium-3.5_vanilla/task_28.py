from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import Langevin
from ase import units

cu = bulk('Cu', 'fcc', a=3.6, cubic=True)
cu = cu.repeat((2, 2, 2))
cu.calc = EMT()

dyn = Langevin(cu, timestep=5 * units.fs, temperature=300, friction=0.01)
dyn.attach(lambda: print(f'T={dyn.get_temperature()/units.kB:6.1f}K'), interval=50)

for temp in range(300, 601, 1):
    dyn.set_temperature(temp * units.kB)
    dyn.run(1)
