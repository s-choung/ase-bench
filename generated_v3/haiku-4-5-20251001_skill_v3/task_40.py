from ase.spacegroup import crystal
from ase.io import write, read

# NaCl 결정 구조 생성 (Rock salt structure, spacegroup 225)
atoms = crystal('NaCl', [(0, 0, 0), (0.5, 0.5, 0.5)], 
                spacegroup=225, cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

# CIF 형식으로 저장
write('nacl.cif', atoms, format='cif')

# CIF 파일 읽기
atoms_read = read('nacl.cif', format='cif')

# 정보 출력
print(f"원자 수: {len(atoms_read)}")
print(f"원자 종류: {atoms_read.get_chemical_symbols()}")
print(f"격자 상수: {atoms_read.get_cell_lengths_and_angles()[:3]}")
