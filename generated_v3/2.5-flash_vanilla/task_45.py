from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# H2 분자 생성
h2 = molecule('H2')

# EMT calculator 설정
h2.set_calculator(EMT())

# Constraint 적용 전 에너지 및 결합 길이 계산
initial_energy = h2.get_potential_energy()
initial_bond_length = h2.get_distance(0, 1)

# FixBondLength constraint 설정 (0.9 옹스트롬)
fixed_length = 0.9
constraint = FixBondLength(0, 1, fixed_length)
h2.set_constraint(constraint)

# Constraint 적용 후 에너지 및 결합 길이 계산
# calculator는 이미 설정되어 있으므로 다시 설정할 필요 없음
constrained_energy = h2.get_potential_energy()
constrained_bond_length = h2.get_distance(0, 1)

# 결과 출력
print(f"Constraint 적용 전 H2 결합 길이: {initial_bond_length:.3f} Å")
print(f"Constraint 적용 전 H2 에너지: {initial_energy:.3f} eV")
print(f"Constraint 적용 후 H2 결합 길이: {constrained_bond_length:.3f} Å")
print(f"Constraint 적용 후 H2 에너지: {constrained_energy:.3f} eV")
