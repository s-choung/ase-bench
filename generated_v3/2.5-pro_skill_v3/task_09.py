from ase.build import bulk
from ase.io import read, write

# 1. Cu FCC bulk 구조 생성
cu_bulk = bulk('Cu', 'fcc', a=3.6, cubic=True)

# 2. VASP POSCAR 형식으로 파일 저장
write('POSCAR', cu_bulk, format='vasp')

# 3. POSCAR 파일 다시 읽기
atoms_read = read('POSCAR', format='vasp')

# 4. 원자 수와 cell parameter 출력
num_atoms = len(atoms_read)
cell_params = atoms_read.get_cell_lengths_and_angles()

print(f"Number of atoms: {num_atoms}")
print(f"Cell parameters [a, b, c, alpha, beta, gamma]: {cell_params}")
