from ase.build import bulk

# 다이아몬드 구조의 Si 단위 셀 생성 (격자상수 5.43 옹스트롬)
lattice_constant = 5.43
si_primitive = bulk('Si', 'diamond', a=lattice_constant)

# 3x3x3 슈퍼셀 생성
supercell = si_primitive * (3, 3, 3)

# 원자 수와 셀 부피 계산
num_atoms = len(supercell)
volume = supercell.get_volume()

# 결과 출력
print(f"Number of atoms: {num_atoms}")
print(f"Cell volume (Angstrom^3): {volume:.2f}")
