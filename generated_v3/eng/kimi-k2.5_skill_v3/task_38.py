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
vib_energies = vib.get_energies()

thermo = HarmonicThermo(vib_energies)
F = thermo.get_helmholtz_energy(300)
print(f"{F:.6f} eV")
