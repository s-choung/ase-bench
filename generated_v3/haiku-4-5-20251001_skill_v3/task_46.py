from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

# Pt(111) slab 생성
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)

# CO 분자 생성 및 흡착
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# 원자 인덱스: slab은 27개(3x3x3), CO는 2개(C, O)
# 하부 1층 고정 (z 좌표가 가장 낮은 9개 원자)
z_coords = slab.get_positions()[:, 2]
bottom_layer_indices = [i for i in range(len(slab)) if z_coords[i] < z_coords.min() + 0.1]

# Constraint 설정
c1 = FixAtoms(indices=bottom_layer_indices)
c2 = FixBondLength(27, 28)  # C(27), O(28) 인덱스

slab.set_constraint([c1, c2])

# Calculator 설정
slab.calc = EMT()

# BFGS 최적화
opt = BFGS(slab, trajectory='opt.traj')
opt.run(fmax=0.05)

# 결과 출력
energy = slab.get_potential_energy()
co_distance = slab.get_distance(27, 28)

print(f"Final energy: {energy:.6f} eV")
print(f"C-O bond length: {co_distance:.6f} Å")
