from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
import numpy as np

# Build Pt(111) slab: 3 layers, 2x2 supercell
slab = fcc111('Pt', size=(2, 2, 3), a=3.92, vacuum=10.0)
slab.pbc = (True, True, False)

# Create CO molecule at fixed bond length 1.15 Å
co = Atoms('CO', positions=[[0., 0., 0.], [0., 0., 1.15]])

# Add CO as adsorbate on top site (above first Pt in center of cell)
# Surface is parallel to xy; add at z relative to slab top
add_adsorbate(slab, co, height=1.85, position='ontop')

# Indices of bottom layer atoms (z coordinate smallest)
z_vals = slab.positions[:, 2]
bottom_indices = np.where(z_vals < z_vals.min() + 0.5)[0].tolist()

# Indices of C and O (last two added atoms)
c_index = len(slab) - 2
o_index = len(slab) - 1

# Set constraints
fix_bottom = FixAtoms(indices=bottom_indices)
fix_co = FixBondLength(c_index, o_index)
slab.set_constraint([fix_bottom, fix_co])

# Calculator
slab.calc = EMT()

# Optimize
opt = BFGS(slab)
opt.run(fmax=0.05)

# Results
final_energy = slab.get_potential_energy()
co_dist = slab.get_distance(c_index, o_index)
print(f'Final energy: {final_energy:.4f} eV')
print(f'C-O distance: {co_dist:.4f} Å')
