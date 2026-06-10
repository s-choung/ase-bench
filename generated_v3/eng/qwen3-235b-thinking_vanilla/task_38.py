from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', cubic=True) * (2, 2, 2)
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)
vib = Vibrations(atoms)
vib.run()
energies = vib.get_energies()[3:] / 1000.0
thermo = HarmonicThermo(energies, potentialenergy=atoms.get_potential_energy())
print(thermo.get_helmholtz_energy(temperature=300) / len(atoms))
