from ase.build import surface, add_vacuum
from ase import Atoms

# Cu bulk에서 (2,1,1) 표면 생성
slab = surface('Cu', indices=(2, 1, 1), layers=3)

# vacuum 10 Å 추가
add_vacuum(slab, vacuum=10.0)

# 원자 수와 cell 출력
print(f"Number of atoms: {len(slab)}")
print(f"Cell:\n{slab.get_cell()}")
