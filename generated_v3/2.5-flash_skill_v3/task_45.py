```python
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# 1. H2 분자 생성
h2 = molecule('H2')
h2.calc = EMT()

# 2. Constraint 적용 전 bond length 및 에너지 계산
initial_bond_length = h2.get_distance(0, 1)
initial_energy = h2.get_potential_energy()

print(f"Constraint 적용 전:")
print(f"  Bond length: {initial_bond_length:.3f} Å")
print(f"  Energy: {initial_energy:.3f} eV")

# 3. 결합 길이를 0.9 옹스트롬으로 수동 조정
# set_distance는 원자 위치를 변경하여 거리를 설정합니다.
