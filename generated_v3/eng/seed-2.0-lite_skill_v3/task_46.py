from ase.build import fcc111, add_adsorbate, molecule
from ase.optimize import BFGS
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT

# Build 3-layer Pt(111) slab
slab = fcc111('Pt', size=(3,3,3), vacuum=10.0)
# Add CO adsorbate ontop site
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Get indices of C and O atoms (last two atoms in slab)
c_idx = len(slab) - 2
o_idx = len(slab) - 1

# Apply constraints: fix bottom layer (tag=1) and fix C-O bond length
fix_bottom = FixAtoms(mask=[atom.tag == 1 for atom in slab])
fix_co = FixBondLength(c_idx, o_idx)
slab.set_constraint([fix_bottom, fix_co])

# Set calculator and optimize
slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

# Output results
final_energy = slab.get_potential_energy()
final_co_dist = slab.get_distance(c_idx, o_idx)
print(f"\nFinal potential energy: {final_energy:.3f} eV")
print(f"Final C-O bond length: {final_co_dist:.3f} Å")
