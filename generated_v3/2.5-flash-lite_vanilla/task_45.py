from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# H2 분자 생성
atoms = Atoms('H2', positions=[(0, 0, 0), (0, 0, 0.7)])

# EMT calculator 설정
calculator = EMT()
atoms.calc = calculator

# constraint 적용 전 에너지 계산
energy_before = atoms.get_potential_energy()
bond_length_before = atoms.get_distance(0, 1)

# FixBondLength constraint 적용 (0.9 옹스트롬)
constraint = FixBondLength(0, 1, 0.9)
atoms.set_constraint(constraint)

# constraint 적용 후 에너지 계산
energy_after = atoms.get_potential_energy()
bond_length_after = atoms.get_distance(0, 1)

# 결과 출력
print(f"Bond length before constraint: {bond_length_before:.4f} Å")
print(f"Energy before constraint: {energy_before:.4f} eV")
print(f"Bond length after constraint: {bond_length_after:.4f} Å")
print(f"Energy after constraint: {energy_after:.4f} eV")
