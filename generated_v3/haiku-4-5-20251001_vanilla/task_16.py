from ase.build import bulk
from ase.visualize import view

# Fe BCC(110) 표면 생성
slab = bulk('Fe', 'bcc', a=2.87, cubic=True)
slab = slab.repeat((2, 2, 4))

# (110) 표면 방향으로 재구성
from ase.build import surface
slab = surface('Fe', (1, 1, 0), 4, vacuum=10.0)

# 원자 수와 cell 크기 출력
print(f"원자 수: {len(slab)}")
print(f"Cell 크기: {slab.cell.cellpar()}")
print(f"Cell 벡터:\n{slab.cell}")
