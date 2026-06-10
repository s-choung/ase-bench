from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.geometry import get_distances

# Setup Pt(111) slab (3 layers)
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')

# Adsorb CO on top site
add_adsorbate(slab, co, height=1.8, position='ontop')

# Identify indices: Pt atoms are indices 0 to (2*2*3)-1, CO atoms are last two
# Fix bottom layer (first 4 atoms in a 2x2x3 slab)
bottom_indices = list(range(4))
fix_slab = FixAtoms(indices=bottom_indices)

# Fix C-O bond (the last two atoms in the Atoms object)
c_idx, o_idx = slab.get_atomic_numbers().shape[0]-2, slab.get_atomic_numbers().shape[0]-1
fix_bond = FixBondLength(c_idx, o_idx)

# Apply both constraints and calculator
slab.set_constraint([fix_slab, fix_bond])
slab.calc = EMT()

# Optimize
opt = BFGS(slab)
opt.run(fmax=0.05)

# Output results
final_energy = slab.get_potential_energy()
co_dist = get_distances(slab.positions[c_idx], slab.positions[o_idx])[0]

print(f"Final Energy: {final_energy:.4f} eV")
print(f"C-O Distance: {co_dist:.4f} Å")
