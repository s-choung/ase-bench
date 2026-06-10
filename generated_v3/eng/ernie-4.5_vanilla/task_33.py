from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create CH4 molecule
molecule = Atoms('CH4', positions=[(0, 0, 0), (1.1, 1.1, 1.1), 
                                    (-1.1, -1.1, 1.1), 
                                    (1.1, -1.1, -1.1), 
                                    (-1.1, 1.1, -1.1)])

# Set EMT calculator
molecule.calc = EMT()

# Optimize the structure
opt = BFGS(molecule)
opt.run(fmax=0.05)

# Perform the vibration calculation
vib = Vibrations(molecule)
vib.run()
vib.summary()

# Filter and print only the real frequencies
frequencies = vib.get_frequencies()
real_frequencies = frequencies[frequencies.imag == 0].real

print("Real frequencies (cm^-1):")
for freq in real_frequencies:
    print(f"{freq:.2f}")
