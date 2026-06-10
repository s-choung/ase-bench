import numpy as np
from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase import Atoms

# 1. Pt(111) 3층 slab 생성
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# 2. CO 분자 생성 및 slab에 흡착
co = Atoms('CO', positions=[(0, 0, 0), (0, 0, 1.14)])
add_adsorbate(slab, co, 1.8, 'ontop')

# 3. Constraint 설정
# 하부 1층(tag=1) 고정
bottom_layer_indices = [atom.index for atom in slab if atom.tag == 1]
fix_bottom = FixAtoms(indices=bottom_layer_indices)

# CO 결합 길이 고정 (C와 O는 마지막 두 원자)
c_index, o_index = len(slab) - 2, len(slab) - 1
fix_co_bond = FixBondLength(c_index, o_index)

# 두 constraint를 동시에 적용
slab.set_constraint([fix_bottom, fix_co_bond])

# 4. Calculator 및 최적화 설정
slab.calc = EMT()
optimizer = BFGS(slab)
optimizer.run(fmax=0.05)

# 5. 결과 출력
final_energy = slab.get_potential_energy()
co_distance = slab.get_distance(c_index, o_index)

print(f"Final potential energy: {final_energy:.4f} eV")
print(f"Final C-O bond distance: {co_distance:.4f} Å")
