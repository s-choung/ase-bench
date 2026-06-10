from ase.build import bulk
from ase.io import write, read

# Cu FCC bulk 생성
atoms = bulk('Cu', 'fcc', a=3.61)

# POSCAR 형식으로 저장
write('POSCAR', atoms, format='vasp')

# POSCAR 읽기
atoms_read = read('POSCAR', format='vasp')

# 원자 수와 cell parameter 출력
print(f"Number of atoms: {len(atoms_read)}")
print(f"Cell parameters (a, b, c, α, β, γ):")
print(atoms_read.get_cell_lengths_and_angles())
