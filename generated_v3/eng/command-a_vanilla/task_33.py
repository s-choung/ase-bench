from ase import Atoms
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.calculators.emt import EMT

# Define CH4 molecule
ch4 = Atoms('CH4', positions=[[0, 0, 0], [1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], calculator=EMT())

# Optimize geometry
dyn = BFGS(ch4, trajectory='ch4_opt.traj')
dyn.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(ch4, name='ch4_vib')
vib.run()
vib.summary()

# Get vibrational frequencies and filter real frequencies
frequencies = vib.get_frequencies()
real_frequencies = [freq for freq in frequencies if freq > 0]

# Print real frequencies
for i, freq in enumerate(real_frequencies):
    print(f'Frequency {i+1}: {freq:.2f} cm-1')
