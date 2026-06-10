from ase.build import fcc111, molecule
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')

add_adsorbate = lambda slab, ads, height, position: slab + ads.translate([0, 0, height])
slab_ads = add_adsorbate(slab, co, 2.0, 'ontop')
slab_ads.calc = EMT()

# Fix bottom layer atoms
fix_bottom = FixAtoms(mask=[a.tag < 3 for a in slab_ads])
slab_ads.set_constraint(fix_bottom)

# Fix C-O bond length
fix_bond = FixBondLength(slab_ads[0], slab_ads[1])
slab_ads.set_constraint(fix_bond)

opt = BFGS(slab_ads, trajectory='opt.traj')
opt.run(fmax=0.05)

print(f"Final energy: {slab_ads.get_potential_energy():.4f} eV")
print(f"C-O distance: {get_distances(slab_ads[0], slab_ads[1])[0]:.4f} Angstroms")
