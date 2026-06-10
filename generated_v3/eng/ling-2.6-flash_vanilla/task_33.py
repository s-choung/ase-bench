from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create CH4 molecule
atoms = Atoms('CH4', positions=[[0, 0, 0], [0.63, 0.63, 0.63], [-0.63, -0.63, 0.63], [-0.63, 0.63, -0.63], [0.63, -0.63, -0.63]])
atoms.set_calculator(EMT())

# Optimize geometry
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(atoms)
vib.summary(d eig=False)

# Extract and print real frequencies
frequencies = vib.get_frequencies()
real_frequencies = frequencies[frequencies.imag == 0].real
print('Real frequencies (cm-1):', sorted(real_frequencies))
