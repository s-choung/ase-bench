from ase.build import bulk, surface, add_vacuum

# 1. Cu bulk 구조 생성
cu_bulk = bulk('Cu', 'fcc', a=3.6, cubic=True)

# 2. (2,1,1) 표면을 3층으로 생성
slab = surface(cu_bulk, (2, 1, 1), 3)

# 3. z 방향으로 10 옹스트롬의 진공 추가
add_vacuum(slab, 10.0)

# 4. 원자 수와 최종 cell 정보 출력
print(f"Number of atoms: {len(slab)}")
print("Final cell:")
print(slab.get_cell())
