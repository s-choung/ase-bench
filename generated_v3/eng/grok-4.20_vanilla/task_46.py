from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
import numpy as np

# Create 3-layer Pt(111) slab
slab = fcc111('Pt', size=(3, 3, 3), vacuum=6.0)

# Add CO on top site
co = slab[-1].position + np.array([0.0, 0.0, 2.0])
slab.append('C')
slab[-1].position = co
slab.append('O')
slab[-1].position = co + np.array([0.0, 0.0, 1.2])

# Constraints: fix bottom layer and C-O bond
bottom = [atom.index for atom in slab if atom.position[2] < 2.0]
constraints = [FixAtoms(indices=bottom),
               FixBondLength(slab[-2].index, slab[-1].index)]
slab.set_constraint(constraints)

slab.calc = EMT()

# Optimize
opt = BFGS(slab, logfile=None)
opt.run(fmax=0.05)

# Results
energy = slab.get_potential_energy()
dist = slab.get_distance(-2, -1)
print(f"Energy: {energy:.4f} eV")
print(f"C-O distance: {dist:.4f} Å")
