from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Define methane molecule
ch4 = Atoms('CH4', positions=[[0, 0, 0], [0, 0, 1.09], 
                              [1.02, 0.4, -0.36], [-1.02, 0.4, -0.36], 
                              [0, 1.02, 0.72]])

# Assign EMT calculator
ch4.calc = EMT()

# Optimize the structure
optimizer = BFGS(ch4)
optimizer.run(fmax=0.01)

# Vibration analysis
vib = Vibrations(ch4)
vib.run()

# Collect and print real vibrations
all_frequencies = vib.get_frequencies()
real_frequencies = [f for f in all_frequencies if f > 0]
print("Real vibrational frequencies (cm^-1):", real_frequencies)

# Clean up
vib.clean()
