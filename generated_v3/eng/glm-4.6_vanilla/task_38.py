from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.61)
atoms.calc = EMT()

vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()
vib.clean()

thermo = HarmonicThermo(freqs=freqs, energyzero=0, potentialenergy=atoms.get_potential_energy())
free_energy = thermo.get_helmholtz_energy(300)
print(f"{free_energy:.6f} eV")
