from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.85, position='ontop')

z = slab.positions[:, 2]
z_sorted = sorted(set(round(v, 6) for v in z))
bottom_z = z_sorted[0]
fix_slab = FixAtoms(mask=[abs(v - bottom_z) < 1e-3 for v in z])

c_idx = len(slab) - 2
o_idx = len(slab) - 1
fix_co = FixBondLength(c_idx, o_idx)

slab.set_constraint([fix_slab, fix_co])
slab.calc = EMT()

opt = BFGS(slab, logfile=None)
opt.run(fmax=0.05)

energy = slab.get_potential_energy()
co_dist = slab.get_distance(c_idx, o_idx)

print(energy)
print(co_dist)
