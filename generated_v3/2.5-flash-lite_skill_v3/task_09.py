from ase.build import bulk
from ase.io import read, write

# Cu FCC bulk 생성
atoms = bulk('Cu', 'fcc', a=3.6)

# VASP POSCAR 형식으로 파일 저장
write('POSCAR', atoms, format='vasp')

# POSCAR 파일 다시 읽기
atoms_read = read('POSCAR', format='vasp')

# 원자 수와 cell parameter 출력
print(f"Number of atoms: {len(atoms_read)}")
print(f"Cell parameters: {atoms_read.get_cell().lengths()}")
