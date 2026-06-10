from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

n_co = len(co)
co_indices = list(range(len(slab) - n_co, len(slab)))
c_idx = co_indices[0]
o_idx = co_indices[1]
if slab[c_idx].symbol != 'C':
    c_idx, o_idx = o_idx, c_idx

fix_bottom = FixAtoms(mask=[a.tag == 3 for a in slab])
fix_co = FixBondLength(c_idx, o_idx)
slab.set_constraint([fix_bottom, fix_co])

slab.calc = EMT()
opt = BFGS(slab, trajectory='pt_co.traj')
opt.run(fmax=0.05)

E = slab.get_potential_energy()
d_co = slab.get_distance(c_idx, o_idx)
print(f"Final energy: {E:.4f} eV")
print(f"C-O distance: {d_co:.4f} Å")
