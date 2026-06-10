from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup
import os

# 1. NaCl 구조 생성
filename = 'nacl.cif'
nacl = bulk('NaCl', 'rocksalt', a=5.64, cubic=True)

# 2. CIF 파일로 저장
write(filename, nacl)

# 3. CIF 파일 다시 읽기
atoms_from_cif = read(filename)

# 4. Spacegroup 정보와 원자 수 출력
sg = get_spacegroup(atoms_from_cif)
num_atoms = len(atoms_from_cif)

print(f"Spacegroup: {sg}")
print(f"Number of atoms: {num_atoms}")

# 5. 생성된 파일 삭제
os.remove(filename)
