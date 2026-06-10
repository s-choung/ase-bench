```python
import os
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db_file = 'metals.db'
if os.path.exists(db_file):
    os.remove(db_file)

# 1. 데이터베이스 생성 및 구조 저장
calc = EMT()
with connect(db_file) as db:
    for symbol in ['Cu', 'Ag', 'Au']:
        atoms = bulk(symbol, 'fcc', cubic=True)
        atoms.set_calculator(calc)
        # db.write()는 계산기가 할당
