import os
from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup
from ase.calculators.emt import EMT

# NaCl 결정 구조 생성 (rocksalt 구조, 격자 상수 a=5.64 옹스트롬)
atoms = bulk('NaCl', 'rocksalt', a=5.64)

# ASE 내장 calculator 부착 (요청에 따라 EMT 사용, 실제 NaCl에는 적합하지 않음)
atoms.calc = EMT()

# CIF 형식으로 저장
filename = 'nacl.cif'
write(filename, atoms)

# CIF 파일 다시 읽어오기
read_atoms = read(filename)

# spacegroup 정보 추출 및 출력
spacegroup = get_spacegroup(read_atoms)
print(f"Spacegroup Number: {spacegroup.no}")
print(f"Spacegroup Symbol: {spacegroup.symbol}")

# 원자 수 출력
print(f"Number of Atoms: {len(read_atoms)}")

# 생성된 CIF 파일 삭제
os.remove(filename)
