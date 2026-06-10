import numpy as np
from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# 1. Create Pt(111) slab (3 layers)
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
slab.calc = EMT()

# 2. Add CO molecule
# CO positions relative to slab surface
add_adsorbate(slab, 'CO', height=1.5, position='ontop')
slab.calc = EMT()

# 3. Define Constraints
# Fix bottom layer (indices 0, 1, 2 are the first layer of atoms in a 3-layer slab)
# In ASE fcc111, atoms are ordered by layer. 
# For 3x3x3 slab, layer 0 is indices 0-8.
bottom_layer_indices = list(range(9))
fix_atoms = FixAtoms(indices=bottom_layer_indices)

# Fix C-O bond length (find indices of C and O)
# We look for the two atoms that are closest to each other in the adsorbate region
# In this specific setup, CO atoms are added last.
c_idx = -2
o_idx = -1
fix_bond = FixBondLength(c_idx, o_idx, 1.128) # Standard CO bond length

slab.set_constraints([fix_atoms, fix_bond])

# 4. Optimization
opt = BFGS(slab, logfile=None)
opt.run(fmax=0.05)

# 5. Output
final_energy = slab.get_potential_energy()
dist = slab.get_distance(c_idx, o_idx)

print(f"Final Energy: {final_energy:.4f} eV")
print(f"C-O Distance: {dist:.4f} Å")
