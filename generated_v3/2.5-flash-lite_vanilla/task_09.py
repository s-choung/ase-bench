from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.io import read, write

# Cu FCC bulk 생성
atoms = fcc111('Cu', size=(2, 2, 2), vacuum=10.0)

# EMT calculator 할당 (VASP POSCAR 형식 저장/읽기에 calculator는 필수 아님)
atoms.calc = EMT()

# VASP POSCAR 형식으로 저장
write('POSCAR_Cu_FCC', atoms, format='vasp')

# VASP POSCAR 형식으로 다시 읽기
atoms_read = read('POSCAR_Cu_FCC', format='vasp')

# 원자 수와 cell parameter 출력
print(f"Number of atoms: {len(atoms_read)}")
print(f"Cell parameters:\n{atoms_read.cell}")
