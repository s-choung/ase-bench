from ase.build import fcc111, add_adsorbate
from ase import Atom
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Pt(111) slab – 3 layers, 3×3 surface cell
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)

# Add CO at a top site
add_adsorbate(slab, 'C', height=1.8, position=(0, 0))
C_idx = len(slab) - 1
z_C = slab[C_idx].z + 1.15
slab.append(Atom('O', (slab[C_idx].x, slab[C_idx].y, z_C)))
O_idx = len(slab) - 1

# Fix bottom layer (tag==2) and C‑O bond
mask_bottom = (slab.get_tags() == 2)
slab.set_constraint([FixAtoms(mask=mask_bottom), FixBondLength(C_idx, O_idx)])

# Optimize with BFGS
slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

# Output
print(f"Final energy: {slab.get_potential_energy():.3f} eV")
print(f"C–O distance: {slab.get_distance(C_idx, O_idx):.3f} Å")
