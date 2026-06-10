from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

# Pt(111) slab, 3 layers
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0, a=3.92)

# Adsorb CO at ontop site
add_adsorbate(slab, molecule('CO'), height=1.85, position='ontop')

# Bottom layer tag (fcc111 tags atoms by layer, bottom = 0)
bottom_tag = min(a.tag for a in slab)
fix_mask = [a.tag == bottom_tag for a in slab]

# CO atoms are appended last: C at -2, O at -1
c_idx, o_idx = len(slab) - 2, len(slab) - 1

# Apply both constraints simultaneously
slab.set_constraint([FixAtoms(mask=fix_mask), FixBondLength(c_idx, o_idx)])

# Optimize
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

print(f"Final energy: {slab.get_potential_energy():.4f} eV")
print(f"C-O distance: {slab.get_distance(c_idx, o_idx):.3f} Å")
