from ase.build import molecule
from ase.geometry import get_distances

# CH4 분자 가져오기
ch4 = molecule('CH4')

# 원자 좌표 출력
print("Atomic Positions (Å):")
print(ch4.get_positions())

# C-H bond lengths 출력
# Carbon은 보통 첫 번째 원자 (index 0)
# Hydrogen은 나머지 원자들 (index 1, 2, 3, 4)
print("\nC-H Bond Lengths (Å):")
for i in range(1, len(ch4)):
    distance = ch4.get_distance(0, i)
    print(f"C({ch4[0].index})-H({ch4[i].index}): {distance:.3f} Å")

# Chemical formula 출력
print("\nChemical Formula:")
print(ch4.get_chemical_formula())
