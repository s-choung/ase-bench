from ase.build import bulk
from ase.io import write, read

# 1. Au FCC bulk 구조 생성
# Au의 격자 상수 (a)는 대략 4.08 Å
atoms = bulk('Au', 'fcc', a=4.08, cubic=True)

# 2. XYZ 형식 파일로 저장
write('au_bulk.xyz', atoms)

# 3. XYZ 파일에서 다시 읽기
read_atoms = read('au_bulk.xyz')

# 4. 원자 종류와 위치 출력
print("원자 종류 (Symbols):")
print(read_atoms.get_chemical_symbols())
print("\n원자 위치 (Positions, Å):")
print(read_atoms.get_positions())
