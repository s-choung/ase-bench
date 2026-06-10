from ase.build import fcc111, make_supercell
from ase.calculators.emt import EMT
from ase.lattice.cubic import FaceCenteredCubic
import numpy as np

# NaCl 결정 구조 생성
a = 5.64
atoms = FaceCenteredCubic(symbol='Na', size=(1, 1, 1), latticeconstant=a)
cl_pos = np.array([0.5, 0.5, 0.5]) * a
atoms.append('Cl', cl_pos)

# 원자 수와 chemical symbols 출력
print(f"Number of atoms: {len(atoms)}")
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")

# EMT calculator 설정 (선택 사항, 계산을 수행하지 않으므로 필수 아님)
atoms.calc = EMT()
