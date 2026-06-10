from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()

thermo = HarmonicThermo(vib.get_energies(), potentialenergy=atoms.get_potential_energy())
print(thermo.get_helmholtz_energy(temperature=300))
