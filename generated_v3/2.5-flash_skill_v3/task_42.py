from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect
import os

# 데이터베이스 파일명
db_filename = 'metals_emt.db'

# 기존 데이터베이스 파일이 있다면 삭제 (스크립트 재실행 시 깨끗한 상태 유지)
if os.path.exists(db_filename):
    os.remove(db_filename)

# ASE 데이터베이스 연결
db = connect(db_filename)

# 금속 정보 (원소 기호, FCC 격자 상수)
metals_info = [
    ('Cu', 3.61),  # Copper FCC lattice constant
    ('Ag', 4.09),  # Silver FCC lattice constant
    ('Au', 4.08),  # Gold FCC lattice constant
]

# 각 금속 bulk 구조 생성, EMT 에너지 계산 및 데이터베이스에 저장
for symbol, a_val in metals_info:
    # bulk 구조 생성
    atoms = bulk(symbol, 'fcc', a=a_val)

    # EMT calculator 설정
    atoms.calc = EMT()

    # 에너지 계산 (이 시점에서 EMT 계산이 수행됨)
    energy = atoms.get_potential_energy()

    # 데이터베이스에 Atoms 객체 저장
    # Atoms 객체와 함께 계산된 에너지, formula 등 기본 정보가 자동으로 저장됨
    db.write(atoms)
    print(f"Saved {symbol} bulk with EMT energy: {energy:.3f} eV")

print("\n--- Database Contents ---")
# 데이터베이스에서 모든 항목 조회 및 formula와 에너지 출력
for row in db.select():
    print(f"Formula: {row.formula}, Energy: {row.energy:.3f} eV")
