from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.optimize import BFGS

# Create N2 molecule
n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]], calculator=EMT())

# Optimize geometry
BFGS(n2).run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(n2, name='n2_vib')
vib.run()
freqs = vib.get_frequencies()

# Print frequencies in cm⁻¹
print("Vibrational frequencies (cm⁻¹):", freqs)
vib.summary()
vib.clean()
