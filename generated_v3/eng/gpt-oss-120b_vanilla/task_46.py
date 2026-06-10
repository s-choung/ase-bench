from ase.build import fcc111, add_adsorbate, molecule
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Pt(111) slab
slab = fcc111('Pt', size=(2, 2), layers=3, vacuum=10.0)

# CO molecule adsorbed on a top site
co = molecule('CO')
add_adsorbate(slab, co, 1.8, slab[-1].position[:2])  # C at 1.8 Å above surface atom
slab.center(vacuum=10.0, axis=2)

# Constraints: fix bottom layer and C–O bond
n_per_layer = len(slab) // 3
fix_bottom = FixAtoms(indices=list(range(n_per_layer)))
c_idx, o_idx = len(slab) - 2, len(slab) - 1
fix_co = FixBondLength(c_idx, o_idx)
slab.set_constraint([fix_bottom, fix_co])

# Calculator & optimization
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

# Output
print('Final energy (eV):', slab.get_potential_energy())
print('C–O distance (Å):', slab.get_distance(c_idx, o_idx))
