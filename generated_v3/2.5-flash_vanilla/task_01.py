from ase.build import bulk

# Cu FCC bulk 생성
cu_bulk = bulk('Cu', 'fcc', a=3.61) # Cu의 격자 상수 (a)는 약 3.61 옹스트롬

# 2x2x2 supercell 생성
cu_supercell = cu_bulk.repeat((2, 2, 2))

# supercell 정보 출력
print("Supercell Cell Information:")
print(cu_supercell.get_cell())
print("\nNumber of atoms in supercell:")
print(len(cu_supercell))
