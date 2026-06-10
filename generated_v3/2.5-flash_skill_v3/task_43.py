from ase.build import fcc111
from ase.db import connect
import os

# 데이터베이스 파일 이름
db_file = 'cu_slabs.db'

# 기존 데이터베이스 파일이 있다면 삭제 (재실행 시 깨끗하게 시작)
if os.path.exists(db_file):
    os.remove(db_file)

# 데이터베이스 연결
db = connect(db_file)

# 다양한 layer 수로 Cu(111) slab 생성 및 저장
for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, layers), vacuum=10.0)
    db.write(slab, layers=layers) # key-value로 layers 정보 저장

# layers=3인 구조만 데이터베이스에서 가져오기
# db.select()는 Row 객체의 이터레이터를 반환하며, .next()로 첫 번째 Row를 가져옴
entry_3_layers = db.select(layers=3).next()
atoms_3_layers = entry_3_layers.toatoms()

# 가져온 구조의 원자 수 출력
print(f"Layers=3인 Cu slab의 원자 수: {atoms_3_layers.get_number_of_atoms()}")
