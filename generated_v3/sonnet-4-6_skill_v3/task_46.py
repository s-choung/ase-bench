from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# 하부 1층 고정 (tag=3이 최하층)
bottom_indices = [a.index for a in slab if a.tag == 3]
fix_atoms = FixAtoms(indices=bottom_indices)

# CO의 C, O 인덱스 (마지막 두 원자)
n = len(slab)
c_idx = n - 2
o_idx = n - 1
fix_bond = FixBondLength(c_idx, o_idx)

slab.set_constraint([fix_atoms, fix_bond])
slab.calc = EMT()

opt = BFGS(slab, trajectory='pt_co.traj')
opt.run(fmax=0.05)

energy = slab.get_potential_energy()
co_dist = slab.get_distance(c_idx, o_idx)

print(f"Final energy: {energy:.4f} eV")
print(f"C-O distance: {co_dist:.4f} Å")
