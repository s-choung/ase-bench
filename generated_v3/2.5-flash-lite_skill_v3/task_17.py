from ase import Atoms
from ase.build import bulk, surface, add_vacuum
from ase.calculators.emt import EMT

# Cu 벌크 생성
cu_bulk = bulk('Cu', 'fcc', a=3.6)

# (2,1,1) 표면 3층으로 생성
slab = surface(cu_bulk, (2, 1, 1), layers=3, vacuum=10.0)

# Vacuum 추가 (surface 함수에서 vacuum 인자로 이미 추가되었지만, 명시적으로 보여주기 위해)
# add_vacuum(slab, 10.0) # surface 함수에서 vacuum 인자로 처리됨

# 계산기 설정 (EMT)
slab.calc = EMT()

# 원자 수와 cell 출력
print(f"Number of atoms: {len(slab)}")
print(f"Cell:\n{slab.get_cell()}")
