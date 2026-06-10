from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase import Atoms
import numpy as np

# Build Pt(111) 3-layer slab with vacuum
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0, a=4.0)

# Tag atoms by layer (bottom layer has z ≈ 0, top layers have larger z)
# fcc111 tags layers from bottom: 0,1,2 for 3-layer slab
# Fix the bottom layer (tag == 0)
bottom_mask = [a.tag == 0 for a in slab]

# Add CO molecule on top
co = molecule('CO')
co.rotate('x', np.pi / 2)  # Align C-O axis with z
add_adsorbate(slab, co, height=2.0, position='ontop')

# CO atoms are the last two added (C index: -2, O index: -1)
c_idx = len(slab) - 2
o_idx = len(slab) - 1

# Apply both constraints
constraints = [
    FixAtoms(mask=bottom_mask),
    FixBondLength(c_idx, o_idx)
]
slab.set_constraint(constraints)

# Calculator and optimization
slab.calc = EMT()
opt = BFGS(slab, trajectory='co_pt_opt.traj')
opt.run(fmax=0.05)

# Results
energy = slab.get_potential_energy()
pos_c = slab.positions[c_idx]
pos_o = slab.positions[o_idx]
bond_length = np.linalg.norm(pos_o - pos_c)

print(f"Final energy: {energy:.4f} eV")
print(f"C-O distance: {bond_length:.4f} A")
