from ase.cluster import Icosahedron
from ase.build import bulk

# Au Icosahedron 나노입자 생성 (noshells=3)
atoms = Icosahedron('Au', noshells=3)

# 원자 수 출력
num_atoms = len(atoms)
print(f"Number of atoms: {num_atoms}")

# Center of Mass 계산 및 출력
# ASE의 get_center_of_mass()는 기본적으로 질량 중심을 계산합니다.
# 모든 원자의 질량이 같다고 가정하면, 단순히 위치의 평균을 구하는 것과 같습니다.
# EMT 계산기를 사용하면 원자 질량을 얻을 수 있습니다.
atoms.calc = bulk('Au', 'fcc', a=0.408).calc # EMT 계산기를 사용하기 위한 임시 설정
com = atoms.get_center_of_mass()
print(f"Center of mass: {com}")
