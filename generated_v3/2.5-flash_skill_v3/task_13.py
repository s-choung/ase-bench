from ase.build import bulk
import numpy as np

# 1. Diamond 구조의 Si bulk 생성
# 'Si' 원소, 'diamond' 구조, 격자상수 a=5.43 옹스트롬
si_bulk = bulk('Si', 'diamond', a=5.43)

# 2. 3x3x3 supercell 생성
si_supercell = si_bulk.repeat((3, 3, 3))

# 3. 원자 수 출력
num_atoms = len(si_supercell)
print(f"Supercell의 원자 수: {num_atoms}")

# 4. Cell volume 출력
cell_volume = si_supercell.get_volume()
print(f"Supercell의 Cell Volume: {cell_volume:.2f} Å³")
