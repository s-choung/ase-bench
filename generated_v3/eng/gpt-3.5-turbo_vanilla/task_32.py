from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Define H2O molecule
atoms = Atoms('H2O', positions=[[0.0, 0.0, 0.0],
                                 [0.757, 0.586, 0.0],
                                 [-0.757, 0.586, 0.0]])
atoms.set_calculator(EMT())

# Calculate vibrational modes
vib = Vibrations(atoms)
vib.run()
vib.summary()

# Print vibrational mode frequencies in cm^-1 and energy in eV
for i, frequency in enumerate(vib.get_frequencies(), 1):
    energy = frequency * 4.135667696e-6  # Convert frequency to eV
    print(f"Mode {i}: Frequency = {frequency:.2f} cm^-1, Energy = {energy:.4f} eV")
