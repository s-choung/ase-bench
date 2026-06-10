from ase.build import bulk

# Cu FCC 단위 셀 생성 (a=3.6 Å)
cu_unit = bulk('Cu', 'fcc', a=3.6, cubic=True)

# 2x2x2 슈퍼셀 생성
cu_supercell = cu_unit * (2, 2, 2)

# 셀 정보와 원자 수 출력
print("Supercell cell vectors (Å):")
print(cu_supercell.cell)
print(f"\nTotal number of atoms: {len(cu_supercell)}")
