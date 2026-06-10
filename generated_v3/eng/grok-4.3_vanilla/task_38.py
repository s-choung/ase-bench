from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
atoms = bulk('Cu')*(2,2,2)
atoms.calc = EMT()
vib = Vibrations(atoms)
vib.run()
ev = vib.get_energies()
thermo = HarmonicThermo(ev[ev>1e-5])
print(thermo.get_helmholtz_energy(300))
