from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton
from ase.vibrations import Vibrations

# Create CH4 molecule
ch4 = Atoms('CH4',
            positions=[[0, 0, 0],
                       [0.63, 0.63, 0.63],
                       [-0.63, -0.63, 0.63],
                       [0.63, -0.63, -0.63],
                       [-0.63, 0.63, -0.63]])

# Set calculator
ch4.calc = EMT()

# Optimize geometry
opt = QuasiNewton(ch4)
opt.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(ch4)
vib.run()
vib.summary()

# Print real frequencies
real_freq = [f for f in vib.get_frequencies() if f.imag == 0]
for f in real_freq:
    print(f.real)

vib.clean()
