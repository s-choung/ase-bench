from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import CrystalThermo

atoms = bulk('Cu', 'fcc') * (2, 2, 2)
atoms.calc = EMT()
BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)
vib = Vibrations(atoms, name='vib')
vib.run()
thermo = CrystalThermo(vib.get_energies(), atoms=atoms, ignore_imaginary_modes=True)
print(thermo.get_helmholtz_energy(temperature=300))
