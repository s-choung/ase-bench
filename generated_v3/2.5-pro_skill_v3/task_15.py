from ase.build import fcc100

# Cu(100) 표면 생성
# size=(3,3,3): 3x3 표면 단위 셀, 3개 원자층
# vacuum=12.0: z축 방향으로 12 옹스트롬의 진공층 추가
slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)

# 원자 수 출력
print(f"Total number of atoms: {len(slab)}")

# 단위 셀 정보 출력
print("Unit cell vectors (Å):")
print(slab.get_cell())
