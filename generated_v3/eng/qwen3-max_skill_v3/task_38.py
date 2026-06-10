from ase import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Create and optimize Cu bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(atoms, name='vib')
vib.run()
freqs = vib.get_frequencies()  # in cm^-1
vib.clean()

# Compute Helmholtz free energy at 300 K
thermo = HarmonicThermo(vib.get_energies())
F = thermo.get_helmholtz_energy(temperature=300.0)
print(F)
