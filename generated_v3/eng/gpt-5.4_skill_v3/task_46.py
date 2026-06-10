from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.85, position='ontop')

bottom_z = sorted(set(slab.positions[:, 2]))[0]
fix_bottom = FixAtoms(mask=[abs(a.position[2] - bottom_z) < 1e-6 for a in slab])

c_idx = len(slab) - 2
o_idx = len(slab) - 1
fix_co = FixBondLength(c_idx, o_idx)

slab.set_constraint([fix_bottom, fix_co])
slab.calc = EMT()

opt = BFGS(slab, logfile=None)
opt.run(fmax=0.05)

energy = slab.get_potential_energy()
co_dist = slab.get_distance(c_idx, o_idx)

print(f'Final energy: {energy:.6f} eV')
print(f'C-O distance: {co_dist:.6f} Å')
