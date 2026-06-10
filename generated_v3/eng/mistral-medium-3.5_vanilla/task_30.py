from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.units import fs
from ase.md.nptberendsen import NPTBerendsen

cu = bulk('Cu', 'fcc', cubic=True)
cu = cu.repeat((3, 3, 3))
cu.calc = EMT()
dyn = NPTBerendsen(cu, timestep=5*fs, temperature=300, pressure=1,
                  taut=100*fs, taup=1000*fs, mask=[1,1,1])
print('Initial volume:', cu.get_volume(), 'Initial pressure:', cu.calc.get_pressure(cu))
dyn.run(200)
print('Final volume:', cu.get_volume(), 'Final pressure:', cu.calc.get_pressure(cu))
