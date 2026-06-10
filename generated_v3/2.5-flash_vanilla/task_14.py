from ase.build import bulk
from ase.calculators.emt import EMT

# NaCl 결정 구조 생성 (rocksalt 구조는 spacegroup 225, Fm-3m에 해당)
# Na는 (0,0,0), Cl은 (0.5,0.5,0.5) 위치에 해당하며 격자상수 5.64 옹스트롬
atoms = bulk('NaCl', 'rocksalt', a=5.64)

# ASE 내장 calculator 부착 (EMT는 예시이며 NaCl에 적합하지 않을 수 있음)
atoms.calc = EMT()

# 원자 수와 chemical symbols 출력
print(f"Number of atoms: {len(atoms)}")
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")
