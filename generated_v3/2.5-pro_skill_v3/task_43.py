import os
from ase.build import fcc111
from ase.db import connect

db_file = 'cu_slabs.db'

# 데이터베이스에 연결하고 구조 생성 및 저장
with connect(db_file) as db:
    for n_layers in [2, 3, 4]:
        slab = fcc111('Cu', size=(2, 2, n_layers), vacuum=8.0)
        # key-value 쌍으로 layer 정보 추가
        db.write(slab, layers=n_layers)

# 데이터베이스에서 특정 조건으로 구조 선택
with connect(db_file) as db:
    # layers=3인 모든 항목을 선택 (이 경우 하나)
    for row in db.select(layers=3):
        atoms3 = row.toatoms()
        print(f"Number of atoms in the 3-layer slab: {len(atoms3)}")

# 생성된 데이터베이스 파일 정리
if os.path.exists(db_file):
    os.remove(db_file)
