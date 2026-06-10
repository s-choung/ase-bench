from ase.db import G2
import numpy as np

# 1. ASE G2 데이터베이스에서 CH4 분자 가져오기
db = G2()
atoms = db.get_atoms('CH4')

print("--- CH4 분자 정보 ---")

# 2. 원자 좌표 출력
print("\n원자 좌표 (Å):")
print(atoms.get_positions())

# 3. Bond lengths 출력
# CH4의 경우 C-H 결합 길이를 찾습니다.
c_indices = [i for i, symbol in enumerate(atoms.get_chemical_symbols()) if symbol == 'C']
h_indices = [i for i, symbol in enumerate(atoms.get_chemical_symbols()) if symbol == 'H']

print("\nBond Lengths:")
if c_indices and h_indices:
    carbon_idx = c_indices[0] # 첫 번째 탄소 원자 인덱스
    for hydrogen_idx in h_indices:
        distance = atoms.get_distance(carbon_idx, hydrogen_idx)
        print(f"C-H bond length ({carbon_idx}-{hydrogen_idx}): {distance:.4f} Å")
else:
    print("C-H 결합 길이를 결정할 수 없습니다 (탄소 또는 수소 원자를 찾을 수 없음).")

# 4. Chemical formula 출력
print("\nChemical Formula:")
print(atoms.get_chemical_formula())
