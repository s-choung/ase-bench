from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

# CH4 분자 생성
atoms = molecule('CH4')

# EMT calculator 설정
atoms.calc = EMT()

# 구조 최적화
optimizer = BFGS(atoms)
optimizer.run(fmax=0.01)

# 진동 계산
vib = Vibrations(atoms, name='ch4_vib')
vib.run()

# 진동 주파수 가져오기 (cm⁻¹)
frequencies = vib.get_frequencies()

# 실수 진동수만 필터링 및 출력
real_frequencies = [freq for freq in frequencies if freq > 0.1] # 0.1 cm⁻¹보다 큰 값만 실수 진동수로 간주

print("Real vibrational frequencies (cm⁻¹):")
for freq in real_frequencies:
    print(f"{freq:.2f}")

# 임시 파일 정리
vib.clean()
