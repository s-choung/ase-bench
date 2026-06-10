import ase.build
import ase.db
import os

# 데이터베이스 파일 이름 정의
db_file = 'cu_slabs.db'

# 기존 데이터베이스 파일이 있다면 삭제 (스크립트 재실행 시 깨끗하게 시작)
if os.path.exists(db_file):
    os.remove(db_file)

# 데이터베이스 연결
db = ase.db.connect(db_file)

# 여러 layer 수로 Cu slab 구조 생성 및 저장
for n_layers in [2, 3, 4]:
    slab = ase.build.fcc111('Cu', size=(2, 2, n_layers), vacuum=10.0)
    db.write(slab, layers=n_layers)

# layers=3인 구조만 선택하여 가져오기
# db.select()는 이터레이터를 반환하므로 next()를 사용하여 첫 번째 항목을 가져옴
entry_3_layers = next(db.select(layers=3))
atoms_3_layers = entry_3_layers.toatoms()

# 선택된 구조의 원자 수 출력
print(f"Number of atoms in the 3-layer slab: {len(atoms_3_layers)}")

# 데이터베이스 연결 종료 (선택 사항, 스크립트 종료 시 자동으로 닫힘)
db.close()
