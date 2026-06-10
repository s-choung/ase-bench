from ase.build import bulk, make_supercell
from ase.calculators.emt import EMT

# 격자 상수 정의
lattice_constant = 5.43

# Si diamond 구조 생성
atoms = bulk('Si', 'diamond', a=lattice_constant)

# 3x3x3 supercell 생성
supercell_matrix = [[3, 0, 0], [0, 3, 0], [0, 0, 3]]
supercell = make_supercell(atoms, supercell_matrix)

# ASE 내장 calculator (EMT) 할당
supercell.calc = EMT()

# 원자 수와 cell volume 출력
print(f"원자 수: {len(supercell)}")
print(f"Cell volume (Å^3): {supercell.get_volume():.2f}")
