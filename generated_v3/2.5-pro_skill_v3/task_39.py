from ase.build import bulk
from ase.io import read, write

# Au FCC bulk 구조 생성 (격자 상수 a=4.08 Å)
au_atoms = bulk('Au', 'fcc', a=4.08, cubic=True)

# XYZ 형식 파일로 저장
filename = 'au_bulk.xyz'
write(filename, au_atoms)

# 파일에서 구조 다시 읽기
atoms_read = read(filename)

# 원자 종류와 위치 출력
print("Symbols:", atoms_read.get_chemical_symbols())
print("Positions:\n", atoms_read.get_positions())
