from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', cubic=True)
atoms.calc = EMT()

BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()

vib_energies = [e.real for e in vib.get_energies() if e.real > 1e-3]
thermo = HarmonicThermo(vib_energies=vib_energies)
F = thermo.get_helmholtz_energy(temperature=300)

print(f"Helmholtz free energy at 300K: {F:.4f} eV")
