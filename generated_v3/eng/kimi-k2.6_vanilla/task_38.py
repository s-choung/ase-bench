from ase.build import bulk
from ase.calculators.emt import EMT
from ase.constraints import ExpCellFilter
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', cubic=True) * (2, 2, 2)
atoms.calc = EMT()
BFGS(ExpCellFilter(atoms)).run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()
energies = vib.get_energies()
energies = energies[energies > 1e-4]

thermo = HarmonicThermo(energies)
F = thermo.get_helmholtz_energy(300)
print(f"{F:.6f} eV")
