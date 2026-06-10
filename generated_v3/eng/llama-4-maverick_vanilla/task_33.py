from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create CH4 molecule
ch4 = Atoms('CH4', positions=[[0, 0, 0], [0.9, 0, 0], [-0.45, 0.7794, 0], [-0.45, -0.3897, 0.675], [-0.45, -0.3897, -0.675]])
ch4.calc = EMT()

# Optimize structure
opt = BFGS(ch4)
opt.run(fmax=0.05)

# Vibration calculation
vib = Vibrations(ch4)
vib.run()
vib.summary()

# Filter and print real frequencies
real_freq = [freq for freq in vib.get_frequencies() if freq > 0]
print("Real frequencies (cm^-1):", real_freq)
