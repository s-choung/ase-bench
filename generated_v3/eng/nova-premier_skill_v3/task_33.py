from ase import Atoms, optimize, units
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
import numpy as np

# Build methane
atoms = Atoms('CH4', positions=[
    [0, 0, 0],
    [0.629, 0.629, 0.629],
    [-0.629, -0.629, 0.629],
    [0.629, -0.629, -0.629],
    [-0.629, 0.629, -0.629]
])

# Optimization
atoms.calc = EMT()
dyn = optimize.BFGS(atoms)
dyn.run(fmax=0.01)

# Vibration analysis
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()

# Filter real frequencies
real_freq = freqs[freqs.real > 0]
print(f"Real frequencies (cm⁻¹): {np.round(real_freq, 2)}")
