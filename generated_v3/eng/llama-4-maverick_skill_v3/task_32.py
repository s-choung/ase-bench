from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create H2O molecule
h2o = Atoms('H2O', positions=[[0, 0, 0], [1, 0, 0], [0, 1, 0]])

# Optimize geometry
h2o.calc = EMT()
opt = BFGS(h2o)
opt.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(h2o)
vib.run()

# Print vibration frequencies and energies
freqs = vib.get_frequencies()
energies = vib.get_energies()
for i, (freq, energy) in enumerate(zip(freqs, energies)):
    print(f"Mode {i+1}: {freq:.2f} cm^-1, {energy:.4f} eV")

# Clean vibration files
vib.clean()
