from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.db import connect

# 데이터베이스 생성 및 연결
db = connect('cu_slab.db')

# 여러 층 수의 Cu slab 생성 및 저장
for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, layers), vacuum=10.0)
    slab.calc = EMT()  # 계산기 설정 (필수는 아니지만, DB에 저장될 수 있음)
    db.write(slab, layers=layers)  # key-value로 layers 정보 저장

# layers=3인 구조만 선택하여 가져오기
selected_slabs = db.select(layers=3)

# 가져온 구조의 원자 수 출력
for slab in selected_slabs:
    print(f"Number of atoms in slab with layers=3: {len(slab)}")
