from ase.build import fcc111, molecule
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.geometry import get_distances

# 1. Build Slab and Adsorbate
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
co = molecule('CO')
from ase.build import add_adsorbate
add_adsorbate(slab, co, height=1.8, position='ontop')

# 2. Set Calculator
slab.calc = EMT()

# 3. Define Constraints
# Fix bottom layer (indices 0 to 8 for a 3x3x3 slab where bottom is first 9 atoms)
# In fcc111(3,3,3), bottom layer atoms are typically 0-8
bottom_layer_indices = [atom.index for atom in slab if atom.tag <= 3] 
# Note: fcc111 build tags layers. layer 1 is tag 1.
fix_bottom = FixAtoms(indices=[a.index for a in slab if a.tag == 1])

# Fix C-O bond length (CO molecule is added at the end, indices 9 and 10)
# Find indices of C and O
c_idx = [a.index for a in slab if a.symbol == 'C'][0]
o_idx = [a.index for a in slab if a.symbol == 'O'][0]
fix_bond = FixBondLength(c_idx, o_idx, get_distances(slab.positions[c_idx], slab.positions[o_idx])[0])

slab.set_constraint([fix_bottom, fix_bond])

# 4. Optimize
opt = BFGS(slab)
opt.run(fmax=0.05)

# 5. Output results
final_energy = slab.get_potential_energy()
dist_co = get_distances(slab.positions[c_idx], slab.positions[o_idx])[0]

print(f"Final Energy: {final_energy:.4f} eV")
print(f"C-O Distance: {dist_co:.4f} Å")
