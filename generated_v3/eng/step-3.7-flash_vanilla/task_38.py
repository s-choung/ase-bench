from ase import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.615).repeat((2, 2, 2))
atoms.calc = EMT()
vib = Vibrations(atoms)
vib.run()
thermo = HarmonicThermo(phonon_modes=vib.get_frequencies())
F = thermo.get_helmholtz_free_energy(T=300) / len(atoms)
print(F)
