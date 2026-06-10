from ase.build import bulk
from ase.io import write, read
import os

# 1. Au FCC bulk 구조 생성
atoms = bulk('Au', 'fcc', a=4.08)

# 2. XYZ 파일로 저장
filename = 'au_fcc.xyz'
write(filename, atoms)

# 3. XYZ 파일에서 다시 읽기
atoms_loaded = read(filename)

# 4. 원자 종류와 위치 출력
print("Atomic symbols:", atoms_loaded.get_chemical_symbols())
print("Atomic positions (in Angstrom):\n", atoms_loaded.get_positions())

# 생성된 파일 삭제 (선택 사항)
os.remove(filename)
