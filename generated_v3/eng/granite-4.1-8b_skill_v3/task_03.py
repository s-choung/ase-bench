from ase import Atoms
from ase.build import mx2
from ase.optimize import BFGS
import numpy as np
from ase.calculators.emt import EMT

# Create a MoS2 monolayer
atoms = mx2('MoS2', kind='2H', thickness=3.17, vacuum=10)

# Optimize the structure (optional, but often recommended)
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.05)

# Add 10 Å of vacuum (already added by mx2, but we can explicitly ensure it)
# Here we simply print the cell size to verify
print("Cell lengths (Å):", np.linalg.norm(atoms.cell, axis=0))
