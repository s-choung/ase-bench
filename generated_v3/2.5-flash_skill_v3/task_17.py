from ase.build import bulk, surface, add_vacuum
from ase import Atoms

# 1. Cu bulk 구조 정의 (FCC, 격자 상수 3.61 Å)
cu_bulk = bulk('Cu', 'fcc', a=3.61)

# 2. (2,1,1) 표면 3층 생성
# surface 함수는 bulk Atoms 객체를 첫 번째 인자로 받거나, 격자 상수 'a'와 격자 종류 'fcc' 등을 직접 지정할 수 있습니다.
# 여기서는 bulk Atoms 객체를 전달하여 격자 정보를 사용합니다.
slab = surface(cu_bulk, indices=(2, 1, 1), layers=3, vacuum=0.0) # vacuum은 add_vacuum으로 나중에 추가

# 3. 진공 10 옹스트롬 추가 (in-place 수정)
add_vacuum(slab, 10.0)

# 4. 원자 수와 cell 출력
print(f"원자 수: {len(slab)}")
print("Cell:")
print(slab.get_cell())
