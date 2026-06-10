from ase.build import bulk
from ase.io import read, write

# Au FCC bulk 구조 생성
au_bulk = bulk('Au', 'fcc', a=4.0782)

# XYZ 파일로 저장
write('au_bulk.xyz', au_bulk)

# XYZ 파일 읽기
au_read = read('au_bulk.xyz')

# 원자 종류와 위치 출력
print("원자 종류:", au_read.get_chemical_symbols())
print("\n원자 위치 (Angstrom):")
for i, (symbol, pos) in enumerate(zip(au_read.get_chemical_symbols(), au_read.get_positions())):
    print(f"{i}: {symbol} {pos}")
