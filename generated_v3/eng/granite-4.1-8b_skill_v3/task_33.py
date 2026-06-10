from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.units import fs

# Create CH4 molecule
symbols = ['C', 'H', 'H', 'H', 'H']
positions = [[0.0, 0.0, 0.0],
             [0.0, 0.0, 1.09],
             [1.08, 0.0, 0.0],
             [-0.54, 0.93, 0.0],
             [-0.54, -0.93, 0.0]]
atoms = Atoms(symbols=symbols, positions=positions, pbc=False)

# Optimize geometry
atoms.calc = EMT()
opt = BFGS(atoms)
opt.run(fmax=0.05)
print('Optimization completed.')

# Vibration calculation
vib = Vibrations(atoms, name='CH4_vib')
vib.run()  # Perform the vibration analysis
vib.summary()
freqs = vib.get_frequencies()  # Frequencies in cm⁻¹ as a numpy array

# Filter only real frequencies
real_freqs = freqs[np.isreal(freqs)]
print('Real vibrational frequencies (cm⁻¹):', real_freqs)
