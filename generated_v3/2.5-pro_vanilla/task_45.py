```python
from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# 1. 제약 조건이 없는 H2 분자 생성 및 계산
h2 = Atoms('H2', positions=[(0, 0, 0), (0, 0, 0.74)])
h2.calc = EMT()

initial_bond_length = h2.get_distance(0, 1)
initial_energy = h2.get_potential_energy()

print("Before constraint:")
print(f"  Bond length: {initial_bond_length:.4f} Å")
print(f"  Energy: {initial_energy:.4f} eV")

# 2. FixBondLength 제약 조건 적용 및 거리 설정
constraint = FixBondLength(0, 1)
h2.set_constraint(constraint)
h2.set_distance(0, 1, 0.9, fix=0)

# 3. 제약 조건 적용 후 에너지 재계산
final_bond_length = h2.get_distance(0, 1)
final_energy = h2.get_potential_energy()

print("\nAfter constraint and setting length to 0.9 Å:")
print(f"  Bond
