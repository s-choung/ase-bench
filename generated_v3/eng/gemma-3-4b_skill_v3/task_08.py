from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.build import molecule

# Create an N2 molecule
n2 = molecule('N2')

# Set the EMT calculator
n2.calc = EMT()

# Optimize the molecule
opt = BFGS(n2)
opt.run(fmax=0.01)

# Run vibrations
vib = Vibrations(n2, name='vib')
vib.run()

# Print the vibrational frequencies
print("Vibrational frequencies (cm⁻¹):")
for freq in vib.get_frequencies():
    print(freq)
