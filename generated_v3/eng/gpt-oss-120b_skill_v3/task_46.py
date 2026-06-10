#!/usr/bin/env python
# ASE script: CO adsorption on Pt(111) slab with dual constraints

from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms, FixBondLength
from ase.geometry import get_distances
import numpy as np

# ----- 1. Build a 3‑layer Pt(111) slab (2×2 surface unit cells)
slab = fcc111('Pt', size=(2, 2, 3), a=3.92, vacuum=10.0)

# ----- 2. Adsorb CO (C first, O second) on an atop site
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')  # in‑place modification

# ----- 3. Identify atoms for constraints
#   a) Bottom layer (tags start at 0 for the top layer)
bottom_tag = max(atom.tag for atom in slab)
fix_bottom = FixAtoms(indices=[i for i, atom in enumerate(slab)
                              if atom.tag == bottom_tag])

#   b) C–O bond (find the two newly added atoms)
co_indices = [i for i, atom in enumerate(slab)
              if atom.symbol in ('C', 'O')]
c_idx, o_idx = co_indices[0], co_indices[1]          # C first, O second
fix_bond = FixBondLength(c_idx, o_idx)

# Apply both constraints simultaneously
slab.set_constraint([fix_bottom, fix_bond])

# ----- 4. Calculator & geometry optimisation
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

# ----- 5. Output final energy and C–O distance
energy = slab.get_potential_energy()
c_pos, o_pos = slab.positions[c_idx], slab.positions[o_idx]
co_dist = np.linalg.norm(c_pos - o_pos)

print(f'Final energy: {energy:.5f} eV')
print(f'C–O distance: {co_dist:.3f} Å')
