from ase.build import molecule

# G2 데이터베이스에서 CH4 분자 구조 가져오기
ch4 = molecule('CH4')

# 1. 원자 좌표 출력 (Å 단위)
print("Atomic Coordinates (Å):")
print(ch4.positions)
print("-" * 30)

# 2. Bond lengths 출력
# C (index 0)와 H (indices 1-4) 사이의 거리 계산
print("Bond Lengths (Å):")
for i in range(1, 5):
    dist = ch4.get_distance(0, i)
    print(f"  C-H bond {i}: {dist:.4f}")
print("-" * 30)

# 3. Chemical formula 출력
formula = ch4.get_chemical_formula()
print(f"Chemical Formula: {formula}")
