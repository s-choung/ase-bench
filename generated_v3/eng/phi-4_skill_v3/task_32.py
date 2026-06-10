from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Step 1: Setup the H2O molecule
atoms = molecule('H2O')

# Set EMT calculator to the molecule
atoms.calc = EMT()

# Step 2: Run optimization with BFGS
bfgs = BFGS(atoms)
bfgs.run(fmax=0.01)  # fmax is the force convergence threshold

# Step 3: Calculate vibrations using EMT
vib = Vibrations(atoms)
vib.run(verbose=True)

# Extract and print the vibrational frequencies and energies
vibrational_frequencies = vib.get_frequencies()
vibrational_energies = vib.get_energies()

# Print each frequency in cm⁻¹ and corresponding energy in eV
print("Vibrational Modes:")
for freq, energy in zip(vibrational_frequencies, vibrational_energies):
    print(f"Frequency: {freq} cm⁻¹")
    print(f"Energy: {energy} eV")
