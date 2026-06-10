from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

# initial tetrahedral CH4 (approx. bond length 1.09 Å)
d = 1.09
pos = [(0, 0, 0),
       ( d,  d,  d),
       ( d, -d, -d),
       (-d,  d, -d),
       (-d, -d,  d)]
atoms = Atoms('CH4', positions=pos, calculator=EMT())

# geometry optimisation
dyn = BFGS(atoms)
dyn.run(fmax=0.01)

# vibrational analysis
vib = Vibrations(atoms)
vib.run()

# keep only real (positive) frequencies
freqs = vib.get_frequencies()
real_freqs = freqs[freqs > 0]

print(real_freqs)
