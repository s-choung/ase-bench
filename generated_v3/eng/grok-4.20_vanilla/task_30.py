from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
from ase.units import fs, bar, kB
from ase.calculators.emt import EMT
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)
atoms *= (3, 3, 3)
atoms.calc = EMT()

print('Initial volume:', atoms.get_volume())

md = NPTBerendsen(atoms, timestep=5*fs, temperature=300, 
                  taut=100*fs, pressure=1*bar, taup=1000*fs,
                  compressibility=4.5e-5)

md.run(200)

print('Final volume:', atoms.get_volume())
print('Final pressure:', atoms.get_stress()[0:3].mean() / bar, 'bar')
