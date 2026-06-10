from ase.db import connect
from ase.build import bulk
from ase.calculators.emt import EMT

# 데이터베이스 생성
db = connect('metals.db')

# Cu bulk 생성 및 저장
cu_bulk = bulk('Cu', 'fcc', a=3.6)
cu_bulk.calc = EMT()
db.write(cu_bulk, formula='Cu', energy=cu_bulk.get_potential_energy())

# Ag bulk 생성 및 저장
ag_bulk = bulk('Ag', 'fcc', a=4.0)
ag_bulk.calc = EMT()
db.write(ag_bulk, formula='Ag', energy=ag_bulk.get_potential_energy())

# Au bulk 생성 및 저장
au_bulk = bulk('Au', 'fcc', a=4.1)
au_bulk.calc = EMT()
db.write(au_bulk, formula='Au', energy=au_bulk.get_potential_energy())

# 데이터베이스에서 모든 항목 조회
results = db.select()

# 각 항목의 formula와 energy 출력
for row in results:
    print(f"Formula: {row.formula}, Energy: {row.energy:.4f} eV")
