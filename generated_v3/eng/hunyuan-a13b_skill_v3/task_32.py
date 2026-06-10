from ase import Atoms
from ase.calculators import EMT
from ase.vibrations import Vibrations

# Define the H2O molecule
atoms = Atoms('O', pos=[[0.0, 0.0, 0.0]],
              'H', pos=[[0.0, 0.757, 0.587],
                       [0.0, -0.757, 0.587]],
              cell=[10, 10, 10], pbc=True, charge=0, spin=0)

# Set EMT calculator
atoms.calc = EMT()

# Optimize geometry
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms, n放松=3)
vib.run()

# Extract frequencies and energies
frequencies = vib.get_frequencies()  # cm^-1
energies = vib.get_energies()      # eV

# Print results
for freq, energy in zip(frequencies, energies):
    print(f"Frequency: {freq:.2f} cm^-1, Energy: {energy:.4f} eV")
