from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

# Create Pt(111) slab
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)

# Add CO molecule on fcc hollow site
co = molecule('CO')
add_adsorbate(slab, co, 1.8, 'hollow')

# Set calculator
slab.calc = EMT()

# Constraints
# Fix bottom layer (layer index 0)
bottom_layer_indices = [atom.index for atom in slab if atom.tag == 0]
fix_bottom = FixAtoms(indices=bottom_layer_indices)

# Fix C-O bond length
# C is the first atom of CO added, O is the second
# Indices depend on slab size: 3x3x3 = 27 atoms. CO added at 27, 28
c_index = len(slab) - 2
o_index = len(slab) - 1
fix_bond = FixBondLength(c_index, o_index)

slab.set_constraint([fix_bottom, fix_bond])

# Optimize
opt = BFGS(slab, trajectory='co_pt111.traj')
opt.run(fmax=0.05)

# Results
energy = slab.get_potential_energy()
co_distance = slab.get_distance(c_index, o_index, mic=True)
print(f'Final Energy: {energy:.4f} eV')
print(f'C-O Distance: {co_distance:.4f} Å')
