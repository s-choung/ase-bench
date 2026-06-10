from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# CH4 geometry (approx tetrahedral)
ch4 = Atoms('CH4',
            positions=[(0.0, 0.0, 0.0),
                       (0.629, 0.629, 0.629),
                       (-0.629, -0.629, 0.629),
                       (-0.629, 0.629, -0.629),
                       (0.629, -0.629, -0.629)],
            calculator=EMT())

# Geometry optimisation
BFGS(ch4, logfile=None).run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(ch4, name='ch4_vib')
vib.run()               # finite‑difference forces
vib.summary()           # prints raw frequencies (including imaginaries)

# Filter and print only real (positive) frequencies
real_freqs = [f for f in vib.get_frequencies() if f > 0]
print('Real vibrational frequencies (THz):')
for f in real_freqs:
    print(f)

vib.cleanup()           # remove temporary files
