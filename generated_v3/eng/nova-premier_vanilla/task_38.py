from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.thermochemistry import HarmonicThermo
from ase.vibrations import Vibrations

cu = Atoms('Cu', positions=[(0, 0, 0)], cell=[3.61, 3.61, 3.61], pbc=True)
cu *= (2, 2, 2)

cu.calc = EMT()
dyn = BFGS(cu)
dyn.run(fmax=0.001)

vib = Vibrations(cu, nfree=2)
vib.run()
vib_energies = vib.get_energies()

thermo = HarmonicThermo(vib_energies)
print(thermo.get_helmholtz_energy(temperature=300))
