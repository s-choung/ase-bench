import numpy as np
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# 1. H2 분자 생성 및 EMT calculator 설정
h2 = molecule('H2')
h2.calc = EMT()

# 2. Constraint 적용 전 bond length와 에너지 계산 및 출력
initial_dist = h2.get_distance(0, 1)
initial_energy = h2.get_potential_energy()

print("--- Before Constraint ---")
print(f"Bond Length: {initial_dist:.4f} Å")
print(f"Potential Energy: {initial_energy:.4f} eV")

# 3. Bond length를 0.9 Å으로 설정하고 FixBondLength constraint 적용
# set_distance()로 거리를 직접 변경. fix=0은 분자 중심을 고정.
h2.set_distance(0, 1, 0.9, fix=0)
constraint = FixBondLength(0, 1)
h2.set_constraint(constraint)

# 4. Constraint 적용 후 bond length와 에너지 계산 및 출력
final_dist = h2.get_distance(0, 1)
final_energy = h2.get_potential_energy()

print("\n--- After Fixing Bond Length to 0.9 Å ---")
print(f"Bond Length: {final_dist:.4f} Å")
print(f"Potential Energy: {final_energy:.4f} eV")
