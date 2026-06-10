from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Create N2 molecule
n2 = Atoms('N2')

# Set the EMT calculator
n2.calc = EMT()

# Optimize geometry (necessary before vibrational analysis)
from ase.optimize import BFGS
opt = BFGS(n2, trajectory='opt.traj')
opt.run(fmax=0.05)

# Perform vibrational frequency analysis
vib = Vibrations(n2)
vib.run()

# Print vibrational frequency values (in cm⁻¹)
frequencies = vib.get_frequencies()
print(frequencies)
