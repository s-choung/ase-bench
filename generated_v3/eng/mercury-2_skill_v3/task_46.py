from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# 3‑layer Pt(111) slab, 2×2 surface cell, 10 Å vacuum
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# remember number of slab atoms before adding CO
n_slab = len(slab)

# CO molecule (C first, O second)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')   # in‑place

# --- constraints -------------------------------------------------
# 1) fix bottom layer (tag == 0) of the original slab only
mask = [atom.tag == 0 and i < n_slab for i, atom in enumerate(slab)]
c_fix_bottom = FixAtoms(mask=mask)

# 2) fix the C–O bond length
iC = n_slab          # index of C atom
iO = n_slab + 1      # index of O atom
c_fix_co = FixBondLength(iC, iO)

slab.set_constraint([c_fix_bottom, c_fix_co])

# --- calculator & optimization ------------------------------------
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

# --- results ------------------------------------------------------
energy = slab.get_potential_energy()
co_dist = slab.get_distance(iC, iO)
print(f'Final energy: {energy:.4f} eV')
print(f'C‑O distance: {co_dist:.4f} Å')
