from ase import Atoms
from ase.vibrations import Vibrations
from ase.calculators.emt import EMT

# Define N2 molecule
n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]], calculator=EMT())

# Relax the structure
n2.get_potential_energy()

# Calculate vibrational frequencies
vib = Vibrations(n2)
vib.run()
vib.summary()

# Print frequencies in cm-1
for freq in vib.get_frequencies():
    print(f"{freq*33.3564:.2f} cm-1")
