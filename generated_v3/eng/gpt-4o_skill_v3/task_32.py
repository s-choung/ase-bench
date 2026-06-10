from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()

# Optimize the geometry
BFGS(atoms).run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms)
vib.run()

# Get frequencies and energies
frequencies = vib.get_frequencies()  # cm^-1
energies = vib.get_energies()        # eV

# Print frequencies and energies
for freq, energy in zip(frequencies, energies):
    print(f"Frequency: {freq:.2f} cm^-1, Energy: {energy:.4f} eV")

vib.clean()
