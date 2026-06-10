import numpy as np
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# 1. N2 분자 구조 생성
atoms = molecule('N2')
atoms.center(vacuum=5.0)

# 2. EMT 계산기 설정
atoms.calc = EMT()

# 3. 구조 최적화 (진동 계산 전 필수)
optimizer = BFGS(atoms, logfile=None)
optimizer.run(fmax=1e-4)

# 4. 진동 분석 수행
vib = Vibrations(atoms, name='vib_n2')
vib.run()

# 5. 진동 주파수 (cm⁻¹) 가져오기 및 출력
frequencies = vib.get_frequencies()
print("Vibrational frequencies (cm^-1):")
print(frequencies)

# 6. 생성된 파일 정리
vib.clean()
