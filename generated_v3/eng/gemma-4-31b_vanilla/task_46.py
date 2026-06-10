from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

# Setup slab
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)

# Setup CO molecule
co = Atoms('CO', positions=[(0, 0, 0), (0, 0, 1.128)])
co.translate([0, 0, 1.5]) # Place above slab center
# Simple approach: move CO to a reasonable site manually or use center of slab
# Shift CO to center of the 3x3 slab surface
cell = slab.get_cell()
co.translate([cell[0,0]/2, cell[1,1]/2, -2.0]) # adjust z later

# Combine
system = slab + co

# Position CO on top of a surface atom
# Finding surface atom index for placement
surf_atom = slab[0] 
co_indices = range(len(slab), len(system))
system[co_indices[0]].position = surf_atom.position + [0, 0, 1.5]
system[co_indices[1]].position = system[co_indices[0]].position + [0, 0, 1.128]

# Constraints
# Fix bottom layer (z=0 approx)
bottom_layer = [atom.index for atom in system if atom.tag == 0 and atom.position[2] < 2.0] # simplify
# Better: Use the build logic, the first layer of the 3-layer slab is the bottom
bottom_indices = range(0, 9) # 3x3 slab bottom layer
fix_bottom = FixAtoms(indices=bottom_indices)

# Fix C-O bond length
fix_bond = FixBondLength(co_indices[0], co_indices[1])

system.set_constraint(fix_bottom)
system.set_constraint(fix_bond)

# Calculator and Optimization
system.calc = EMT()
opt = BFGS(system, trajectory='opt.traj')
opt.run(fmax=0.05)

# Results
final_energy = system.get_potential_energy()
co_dist = system.get_distance(co_indices[0], co_indices[1])

print(f"Final Energy: {final_energy:.4f} eV")
print(f"C-O Distance: {co_dist:.4f} Å")
