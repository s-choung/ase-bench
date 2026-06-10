from ase.build import fcc111
from ase.io import read, write
from ase.calculators.emt import EMT
from ase.spacegroup import Spacegroup

# NaCl 결정 구조 생성
atoms = fcc111('NaCl', size=(2, 2, 1), vacuum=10)

# EMT 계산기 설정 (계산은 실제로 수행하지 않음, 구조 정보만 사용)
atoms.calc = EMT()

# CIF 파일로 저장
write('nacl.cif', atoms)

# CIF 파일에서 구조 읽어오기
read_atoms = read('nacl.cif')

# Spacegroup 정보 추출 및 출력
sg = Spacegroup(read_atoms.cell.get_cellpar())
print(f"Spacegroup: {sg.no} ({sg.symbol})")

# 원자 수 출력
print(f"Number of atoms: {len(read_atoms)}")
