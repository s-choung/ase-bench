from ase.build import bulk
from ase.calculators.emt import EMT

# Cu FCC bulk 2x2x2 supercell 생성
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)
atoms = atoms.repeat((2, 2, 2))

# Calculator 설정
atoms.calc = EMT()

# 0번 원자와 나머지 모든 원자 사이의 거리 계산
distances = atoms.get_distances(0, range(len(atoms)), mic=True)

# 최소 거리와 최대 거리 출력
print(f"최소 거리: {distances[1:].min():.4f} Å")
print(f"최대 거리: {distances[1:].max():.4f} Å")
print(f"0번 원자와의 거리 (처음 10개): {distances[:10]}")
