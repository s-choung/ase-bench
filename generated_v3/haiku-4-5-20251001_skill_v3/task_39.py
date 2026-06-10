from ase.build import bulk
from ase.io import write, read

# Au FCC bulk 생성
atoms = bulk('Au', 'fcc', a=4.0782)

# XYZ 형식으로 저장
write('au_bulk.xyz', atoms)

# XYZ 파일 읽기
atoms_read = read('au_bulk.xyz')

# 원자 종류와 위치 출력
print("원자 종류:", atoms_read.get_chemical_symbols())
print("\n원자 위치 (Å):")
for i, (symbol, pos) in enumerate(zip(atoms_read.get_chemical_symbols(), atoms_read.get_positions())):
    print(f"{i}: {symbol} {pos}")
