from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS
from ase.thermochemistry import HarmonicThermo
from ase.vibrations import Vibrations

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()
BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)

vib = Vibrations(atoms, name='vib')
vib.run()
vib.summary()

vib_energies = vib.get_energies()
thermo = HarmonicThermo(vib_energies=vib_energies)
F = thermo.get_helmholtz_energy(temperature=300, verbose=False)
print(f'Helmholtz free energy at 300 K: {F:.6f} eV')

vib.clean()
