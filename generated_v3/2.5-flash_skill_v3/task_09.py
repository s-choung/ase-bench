from ase.build import bulk
from ase.io import write, read
import os

# 1. Cu FCC bulk 구조 생성
cu_bulk = bulk('Cu', 'fcc', a=3.6)

# 2. VASP POSCAR 형식으로 파일 저장
write('POSCAR', cu_bulk, format='vasp')

# 3. 저장된 POSCAR 파일 읽기
read_atoms = read('POSCAR', format='vasp')

# 4. 원자 수와 cell parameter 출력
print(f"읽어온 구조의 원자 수: {len(read_atoms)}")
cell_lengths_angles = read_atoms.get_cell_lengths_and_angles()
print(f"Cell lengths (a, b, c): {cell_lengths_angles[0]:.3f}, {cell_lengths_angles[1]:.3f}, {cell_lengths_angles[2]:.3f} Å")
print(f"Cell angles (alpha, beta, gamma): {cell_lengths_angles[3]:.2f}, {cell_lengths_angles[4]:.2f}, {cell_lengths_angles[5]:.2f} degrees")

# 생성된 POSCAR 파일 삭제 (선택 사항)
os.remove('POSCAR')
