from ase.build import bulk, surface

# Cu bulk 생성 (fcc, a=3.61 Å)
cu_bulk = bulk('Cu', 'fcc', a=3.61)

# (2,1,1) 표면을 3층으로 자르고 vacuum 10 Å 추가
cu_211_surface = surface(cu_bulk, (2, 1, 1), 3, vacuum=10.0)

# 원자 수와 cell 정보 출력
print(f"Number of atoms: {len(cu_211_surface)}")
print("Cell vectors:")
print(cu_211_surface.cell)
