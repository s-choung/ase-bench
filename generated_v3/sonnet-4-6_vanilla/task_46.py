from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

add_adsorbate(slab, 'C', height=1.8, position='ontop')
add_adsorbate(slab, 'O', height=3.0, position='ontop')

n_slab = 12
c_idx = n_slab
o_idx = n_slab + 1

bottom_layer_indices = [i for i in range(4)]

fix_bottom = FixAtoms(indices=bottom_layer_indices)
fix_co = FixBondLength(c_idx, o_idx)

slab.set_constraint([fix_bottom, fix_co])
slab.calc = EMT()

opt = BFGS(slab, trajectory='pt111_co.traj')
opt.run(fmax=0.05)

energy = slab.get_potential_energy()
c_pos = slab.positions[c_idx]
o_pos = slab.positions[o_idx]
co_dist = ((c_pos - o_pos)**2).sum()**0.5

print(f"Final energy: {energy:.4f} eV")
print(f"C-O bond length: {co_dist:.4f} Å")
