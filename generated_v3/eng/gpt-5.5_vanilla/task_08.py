from tempfile import TemporaryDirectory

from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

n2 = Atoms("N2", positions=[(0, 0, 0), (0, 0, 1.10)])
n2.center(vacuum=5.0)
n2.calc = EMT()

BFGS(n2, logfile=None).run(fmax=0.01)

with TemporaryDirectory() as tmpdir:
    vib = Vibrations(n2, name=f"{tmpdir}/n2")
    vib.run()
    for freq in vib.get_frequencies():
        print(freq)
    vib.clean()
