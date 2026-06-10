from ase.build import nanotube
from ase import units

# (6,6) 탄소 나노튜브 생성, 길이 4 옹스트롬
atoms = nanotube(n=6, m=6, length=4*units.angstrom)

# 원자 수 출력
print(f"Number of atoms: {len(atoms)}")

# 셀 정보 출력
print(f"Cell:\n{atoms.get_cell()}")
