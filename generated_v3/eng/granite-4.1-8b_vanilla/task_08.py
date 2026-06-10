from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create N2 molecule
n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])

# Attach EMT calculator
n2.calc = EMT()

# Relax the molecule to find the equilibrium geometry
relax = BFGS(n2)
relax.run(fmax=0.005)

# Perform vibrational analysis
vib = Vibrations(n2)
vib.run(check_interval=10, constraint=None)
vib.write("vibrations.out")

# Extract and print vibrational frequencies (in cm^-1)
freqs = vib.get_frequencies() * 100  # Convert from Hz to cm^-1
print(freqs)
