from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Create N2 molecule
N2 = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
N2.set_calculator(EMT())

# Calculate vibrational frequencies
vib = Vibrations(N2)
vib.run()
frequencies = vib.get_energies()
print(frequencies)
