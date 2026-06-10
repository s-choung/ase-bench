from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create CH4 molecule
ch4 = Atoms('CH4', positions=[
    (0, 0, 0),
    (0.89, 0.89, 0.89),
    (-0.89, -0.89, 0.89),
    (-0.89, 0.89, -0.89),
    (0.89, -0.89, -0.89)
])

# Optimize the structure
ch4.calc = EMT()
opt = BFGS(ch4)
opt.run(fmax=0.01)

# Vibration calculation
vib = Vibrations(ch4, name='vib_ch4')
vib.run()

# Get frequencies and filter real ones
freqs = vib.get_frequencies()
real_freqs = freqs[freqs > 0]

# Print real frequencies
print(real_freqs)

# Clean up vibration files
vib.clean()
