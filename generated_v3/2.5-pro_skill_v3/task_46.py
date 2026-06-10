import numpy as np
from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

# 1. Pt(111) 3층 slab 생성 (fcc111은 자동으로 layer tag를 1, 2, 3으로 지정)
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# 2. CO 분자 생성 및 on-top 위치에 흡착
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# 3. EMT calculator 설정
slab.calc = EMT()

# 4. Constraint 설정
# 하부 1층(tag=1) 고정
c1 = FixAtoms(mask=[atom.tag == 1 for atom in slab])

# CO 분자(마지막 두 원자)의 결합 길이 고정
c_idx, o_idx = len(slab) - 2, len(slab) - 1
c2 = FixBondLength(c_idx, o_idx)

# 두 constraint를 동시에 적용
slab.set_constraint([c1, c2])

# 5. 구조 최적화 실행
optimizer = BFGS(slab, trajectory='pt_co_opt.traj')
optimizer.run(fmax=0.05)

# 6. 최종 에너지와 C-O 거리 출력
final_energy = slab.get_potential_energy()
final_co_distance = slab.get_distance(c_idx, o_idx)

print(f"Final potential energy: {final_energy:.4f} eV")
print(f"Final C-O distance: {final_co_distance:.4f} Å")
