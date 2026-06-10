from ase.build import bulk
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
import ase.units as u

atoms = bulk('Cu', 'fcc') * (2, 2, 2)
atoms.calc = EMT()
s, e, n = 300, 600, 200
i = 0
T = s
def ramp():
    global i, T
    T = s + (e - s) * i / (n - 1)
    i += 1
    return T
dyn = Langevin(atoms, 5 * u.fs, ramp, logfile=None, trajectory=None)
dyn.attach(lambda: print(f"Step {dyn.nsteps}: {T:.1f} K"), interval=50)
dyn.run(200)
