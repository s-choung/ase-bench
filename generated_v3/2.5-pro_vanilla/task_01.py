```python
from ase.build import bulk

# Cu FCC 구조 생성 및 2x2x2 supercell 확장
# 실험적인 Cu 격자 상수 사용 (a=3.61 Å)
cu_supercell = bulk('Cu', crystalstructure='fcc', a=3.61) * (2, 2, 2)

# Cell 정보 출력
print("Cell information:")
print(cu_supercell.cell)

# 원자 수
