from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import fcc111, molecule

# Al(111) slab 생성
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# N2 분자 생성
n2 = molecule('N2')

# N2 분자를 slab의 bridge 사이트에 흡착
# bridge 사이트의 위치를 찾기 위해 slab의 원자 좌표를 이용
# 여기서는 간단하게 slab의 중심 근처 bridge 위치를 가정
# 실제로는 더 정교한 위치 탐색이 필요할 수 있음
bridge_pos = (slab.cell.array[0] / 2 + slab.cell.array[1] / 2 + slab.positions[0])
n2.translate(bridge_pos)
n2.translate([0, 0, 2.0]) # 흡착 높이 설정

# slab과 N2 분자를 합침
atoms = slab + n2

# EMT calculator 설정
atoms.calc = EMT()

# 최종 구조의 원자 수와 원자 종류 출력
print(f"Number of atoms: {len(atoms)}")
print(f"Atom types: {atoms.get_chemical_symbols()}")
