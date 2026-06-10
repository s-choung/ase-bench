from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Initialize CH4 molecule and assign calculator
atoms = molecule('CH4')
atoms.calc = EMT()

# Optimize geometry first
BFGS(atoms, trajectory='ch4_opt.traj').run(fmax=0.01)

# Run vibrational analysis
vib = Vibrations(atoms, name='ch4_vib')
vib.run()
all_freqs = vib.get_frequencies()

# Filter out imaginary (negative) frequencies, retain only real values
real_frequencies = [f for f in all_freqs if f > 1e-3]
print("Real vibrational frequencies (cm⁻¹):", real_frequencies)

# Clean up temporary calculation files
vib.clean()
