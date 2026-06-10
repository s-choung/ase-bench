from ase.build import fcc111, bulk
from ase.visualize import view

# Cu FCC bulk 생성
cu_bulk = bulk('Cu', 'fcc', a=3.61)

# 2x2x2 supercell 생성
cu_supercell = cu_bulk.repeat((2, 2, 2))

# cell 정보 출력
print("Cell:", cu_supercell.cell)

# 원자 수 출력
print("Number of atoms:", len(cu_supercell))
