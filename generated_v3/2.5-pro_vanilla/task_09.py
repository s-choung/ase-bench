```python
from ase.build import bulk
from ase.io import read, write

# 1. Cu FCC bulk 구조 생성 (conventional cell)
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)

# 2. VASP POSCAR 형식으로 파일
