from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.io import read, write

# Au FCC bulk 생성
atoms = fcc111('Au', size=(2, 2, 2), vacuum=10.0)
atoms.calc = EMT()

# XYZ 형식으로 저장
write('au_fcc_bulk.xyz', atoms)

# XYZ 파일 읽기
read_atoms = read('au_fcc_bulk.xyz')

# 원자 종류와 위치 출력
for atom in read_atoms:
    print(f"Element: {atom.symbol}, Position: {atom.position}")
