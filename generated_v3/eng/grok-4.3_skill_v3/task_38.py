from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)
atoms = atoms.repeat((2,2,2))
atoms.calc = EMT()
vib = Vibrations(atoms)
vib.run()
energies = vib.get_energies()
F = HarmonicThermo(energies).get_helmholtz_free_energy(300)
print(F)
