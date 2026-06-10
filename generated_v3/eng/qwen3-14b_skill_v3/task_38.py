from ase import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', cubic=True)
atoms.calc = EMT()

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()
energies = vib.get_energies()

thermo = HarmonicThermo(vib_energies=energies, atoms=atoms, temperature=300)
print(thermo.get_helmholtz_energy())
