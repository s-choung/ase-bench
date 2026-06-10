from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)

vib = Vibrations(atoms, name='vib_cu')
vib.run()
vib.summary()

vib_energies = vib.get_energies()
real_energies = [e.real for e in vib_energies if e.real > 0 and abs(e.imag) < 1e-8]

thermo = HarmonicThermo(vib_energies=real_energies)
F = thermo.get_helmholtz_energy(temperature=300)

print(f"\nHelmholtz free energy at 300 K: {F:.6f} eV")

vib.clean()
