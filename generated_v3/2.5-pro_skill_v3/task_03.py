from ase.build import mx2

# MoS2 단층(monolayer) 구조 생성 (2H상)
# z-방향으로 10 옹스트롬의 진공층을 포함
atoms = mx2('MoS2', kind='2H', vacuum=10.0)

# 생성된 구조의 cell 크기 (cell vectors) 출력
print("Cell vectors (Å):")
print(atoms.cell)

# cell 길이와 각도 [a, b, c, alpha, beta, gamma] 출력
print("\nCell lengths (Å) and angles (°):")
print(atoms.get_cell_lengths_and_angles())
