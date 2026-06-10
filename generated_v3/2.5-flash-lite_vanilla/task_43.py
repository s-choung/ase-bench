from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.db import connect

# Database 파일 생성
db = connect('cu_slabs.db')

# Cu slab 구조 생성 및 저장 (2, 3, 4층)
for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, layers), vacuum=10)
    slab.calc = EMT()  # EMT calculator 할당 (필수는 아니지만 예시로 포함)
    db.write(slab, layers=layers)

# layers=3인 구조만 선택하여 원자 수 출력
selected_slabs = db.select(layers=3)
for row in selected_slabs:
    atoms = row.toatoms()
    print(f"Layers: {row.layers}, Number of atoms: {len(atoms)}")
