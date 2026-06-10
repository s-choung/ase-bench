from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Create H2O molecule
h2o = molecule('H2O')
h2o.set_calculator(EMT())

# Vibrational analysis
vib = Vibrations(h2o)
vib.run()
freqs = vib.get_frequencies()   # in cm^-1
energies = vib.get_energies()   # in eV

# Print vibrational modes (excluding near-zero translational/rotational)
for i, (f, e) in enumerate(zip(freqs, energies)):
    if abs(f) > 1e-2:  # filter out translations/rotations
        print(f"Mode {i}: {f:.2f} cm^-1, {e:.4f} eV")
