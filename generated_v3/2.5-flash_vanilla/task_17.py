from ase.build import bulk, surface
from ase.calculators.emt import EMT

# Cu bulk 생성
cu_bulk = bulk('Cu', 'fcc', a=3.61)
cu_bulk.calc = EMT()

# (2,1,1) 표면을 3층으로 자르고 10 옹스트롬 진공 추가
cu_surface = surface(cu_bulk, miller_index=(2,1,1), layers=3, vacuum=10.0)

# 원자 수와 cell 출력
print(f"Number of atoms: {len(cu_surface)}")
print(f"Cell:\n{cu_surface.get_cell()}")
