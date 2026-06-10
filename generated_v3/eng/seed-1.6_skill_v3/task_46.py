from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.geometry import get_distances

# Build Pt(111) 3-layer slab
slab = fcc111('Pt', size=(2,2,3), vacuum=10.0)
# Add CO adsorbate
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')
# Define constraints: fix bottom layer & C-O bond
fix_bottom = FixAtoms(mask=[a.tag == 0 for a in slab])
c_idx, o_idx = slab[-2].index, slab[-1].index
fix_cobond = FixBondLength(c_idx, o_idx)
slab.set_constraint([fix_bottom, fix_cobond])
# Optimize
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)
# Print results
print(f'Final energy: {slab.get_potential_energy():.3f} eV')
print(f'C-O distance: {get_distances(slab.positions, indices=[c_idx], cell=slab.cell, pbc=slab.pbc)[1][0][o_idx]:.3f} Å')
