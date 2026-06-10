from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Setup H2O molecule and calculator
atoms = molecule('H2O')
atoms.calc = EMT()

# Structure relaxation is required before vibrations
BFGS(atoms).run(fmax=0.01)

# Calculate vibrational modes
vib = Vibrations(atoms, name='h2o_vib')
vib.run()

# Retrieve frequencies (cm^-1) and energies (eV)
freqs = vib.get_frequencies()
energies = vib.get_energies()

for f, e in zip(freqs, energies):
    print(f"Frequency: {f:.2f} cm^-1, Energy: {e:.4f} eV")

vib.clean()
