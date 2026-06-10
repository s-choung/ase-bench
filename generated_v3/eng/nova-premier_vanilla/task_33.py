from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Create methane molecule
ch4 = Atoms('CH4', positions=[[0, 0, 0], [0, 0, 1.09], [1.026, 0, -0.363], 
                           [-0.513, -0.889, -0.363], [-0.513, 0.889, -0.363]])

# EMT calculator
ch4.calc = EMT()

# Optimize structure
dyn = BFGS(ch4)
dyn.run(fmax=0.05)

# Vibrational analysis
vib = Vibrations(ch4)
vib.run()

# Print real frequencies
real_freqs = [f for f in vib.get_frequencies() if f > 0]
print("Real frequencies (cm^-1):", real_freqs)
