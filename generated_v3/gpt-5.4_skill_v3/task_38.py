from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

BFGS(FrechetCellFilter(atoms), logfile=None).run(fmax=0.01)
BFGS(atoms, logfile=None).run(fmax=0.01)

vib = Vibrations(atoms, name='cu_bulk_vib')
vib.run()
vib_energies = vib.get_energies()
vib.clean()

thermo = HarmonicThermo(vib_energies=vib_energies)
F = thermo.get_helmholtz_energy(temperature=300.0, verbose=False)

print(f"{F:.6f} eV")
