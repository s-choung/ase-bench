from ase.io import write
from ase.build import molecule
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Create CH4 molecule and set EMT calculator
atoms = molecule('CH4')
atoms.calc = EMT()

# Optimize the structure
opt = BFGS(atoms, trajectory='opt.traj')
opt.run(fmax=0.05)

# Run vibration analysis
vib = Vibrations(atoms, name='vib')
vib.run()
freqs = vib.get_frequencies()

# Extract and output real frequencies (positive values)
real_freqs = freqs[freqs > 0]
print("# Real vibrational frequencies (cm⁻¹):")
for i, f in enumerate(real_freqs, 1):
    print(f"{i}: {f:.1f}")

# Clean temporary vibration files
vib.clean()
