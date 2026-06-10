from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.vibrations import Vibrations
import numpy as np

# CH4: C at center, H at tetrahedral vertices
atoms = Atoms('CH4', positions=[
    [0.0, 0.0, 0.0],
    [0.63, 0.63, 0.63],
    [0.63, -0.63, -0.63],
    [-0.63, 0.63, -0.63],
    [-0.63, -0.63, 0.63]
], cell=[[-6, -6, -6], [-6, 6, 6], [6, -6, 6]])

# Fix C at center to keep orientation
fix = FixAtoms(mask=[0])
atoms.set_constraint(fix)

atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()
real_freqs = freqs[np.isreal(freqs)]
print(real_freqs)
