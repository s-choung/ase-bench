import os
from ase.spacegroup import crystal
from ase.io import write, read
from ase.spacegroup import get_spacegroup

# 1. NaCl 결정 구조 생성 (Spacegroup 225, Fm-3m)
nacl = crystal(['Na', 'Cl'],
               basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
               spacegroup=225,
               cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

# 2. CIF 파일로 저장
cif_file = 'nacl.cif'
write(cif_file, nacl, format='cif')

# 3. CIF 파일 다시 읽기
nacl_read = read(cif_file)

# 4. Spacegroup 정보와 원자 수 출력
sg = get_spacegroup(nacl_read, symprec=1e-4)
num_atoms = len(nacl_read)

print(f"CIF 파일: {cif_file}")
print(f"Spacegroup Number: {sg.no}")
print(f"Spacegroup Symbol: {sg.symbol}")
print(f"Number of atoms in unit cell: {num_atoms}")

# 생성된 파일 삭제
os.remove(cif_file)
