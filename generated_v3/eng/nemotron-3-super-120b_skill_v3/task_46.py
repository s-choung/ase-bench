from ase import Atoms
from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Pt(111) slab, 3 layers, 2x2 surface cell, 10 Å vacuum
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# CO molecule
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')  # slab modified in‑place

# Identify bottom layer (lowest z)
zs = slab.get_positions()[:, 2]
bottom_mask = zs < zs.min() + 0.1
bottom_indices = [i for i, flag in enumerate(bottom_mask) if flag]

# Indices of C and O atoms (added last)
c_idx = len(slab) - 2
o_idx = len(slab) - 1

# Apply both constraints
slab.set_constraint([FixAtoms(indices=bottom_indices),
                     FixBondLength(c_idx, o_idx)])

# Calculator
slab.calc = EMT()

# Optimization
BFGS(slab).run(fmax=0.05)

# Results
energy = slab.get_potential_energy()
co_dist = slab.get_distance(c_idx, o_idx)
print(f'Final energy: {energy:.4f} eV')
print(f'C-O distance: {co_dist:.4f} Å')
