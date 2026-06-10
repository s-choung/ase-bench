from ase.build import nanotube
from ase import Atoms

# Carbon nanotube (6,6) 생성
cnt = nanotube(6, 6, length=4)

# 원자 수
print(f"Number of atoms: {len(cnt)}")

# Cell 정보
cell = cnt.get_cell()
print(f"Cell:\n{cell}")
print(f"Cell lengths: {cnt.get_cell_lengths_and_angles()[:3]}")
print(f"Cell angles: {cnt.get_cell_lengths_and_angles()[3:]}")

# PBC 확인
print(f"PBC: {cnt.pbc}")
