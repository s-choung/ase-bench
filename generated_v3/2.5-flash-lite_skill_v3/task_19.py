from ase import Atoms
from ase.calculators.emt import EMT
from ase.geometry import get_distances

# CO2 분자 생성
# C를 원점에, O를 양쪽 1.16 옹스트롬에 배치
positions = [(0.0, 0.0, 0.0), (-1.16, 0.0, 0.0), (1.16, 0.0, 0.0)]
symbols = ['C', 'O', 'O']
cell = (10, 10, 10)
pbc = False

atoms = Atoms(symbols=symbols, positions=positions, cell=cell, pbc=pbc)

# 원자 간 거리 계산 및 출력
distances = get_distances(atoms.get_positions())
print("Distances between atoms (in Angstrom):")
print(distances)

# EMT 계산기 설정 (선택 사항, 계산을 위해 필요)
atoms.calc = EMT()
