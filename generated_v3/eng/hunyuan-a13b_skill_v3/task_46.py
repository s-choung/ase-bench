from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.atom import Atom
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators import EMT
from ase.optimize import BFGS

# Build Pt(111) slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
slab.set_cell(slab.get_cell().scale(1.0))  # Ensure lattice parameters are correct

# Add CO molecule
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Generate atom indices for constraints
bottom_layer_mask = [atom.index < 4 for atom in slab]  # Bottom layer indices
fix_bottom = FixAtoms(mask=bottom_layer_mask)

# Fix C-O bond (find indices of C and O in slab)
c_atom = slab()[slab.symbols == 'C'][0]
o_atom = slab()[slab.symbols == 'O'][0]
fix_cobond = FixBondLength(slab.cell, c_atom.index, o_atom.index)

# Apply constraints
slab.set_constraint([fix_bottom, fix_cobond])

# Set up calculator and optimizer
slab.calc = EMT()
opt = BFGS(slab, trajectory='opt.traj')
opt.set_fmax(0.05)
opt.run()

# Calculate final energy and C-O distance
final_energy = slab.get_potential_energy()
c_o_distance = slab.get_distance(c_atom.index, o_atom.index)

print(f"Final Energy: {final_energy} eV")
print(f"C-O Distance: {c_o_distance} Å")
