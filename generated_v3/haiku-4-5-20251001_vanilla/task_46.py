from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import write

# Pt(111) 3층 slab 생성
slab = fcc111('Pt', size=(4, 4, 3), a=3.92, vacuum=10.0)

# CO 분자 흡착 (top site)
add_adsorbate(slab, 'CO', height=1.2, position='ontop')

# Constraint 1: 하부 1층 고정
fixed_mask = slab.positions[:, 2] < slab.positions[:, 2].min() + 1.0
constraint1 = FixAtoms(mask=fixed_mask)

# CO의 C와 O 인덱스 찾기 (마지막 두 원자)
c_index = len(slab) - 2
o_index = len(slab) - 1

# Constraint 2: C-O 결합 길이 고정
constraint2 = FixBondLength(c_index, o_index)

# 두 constraint 동시 적용
slab.set_constraint([constraint1, constraint2])

# Calculator 설정
slab.set_calculator(EMT())

# BFGS 최적화
dyn = BFGS(slab, trajectory='opt.traj')
dyn.run(fmax=0.05)

# 최종 에너지
final_energy = slab.get_potential_energy()

# C-O 거리
co_distance = slab.get_distance(c_index, o_index)

print(f"Final Energy: {final_energy:.6f} eV")
print(f"C-O Bond Length: {co_distance:.6f} Å")
