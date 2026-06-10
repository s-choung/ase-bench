import numpy as np
from ase import build
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.vibrations import Vibrations

# 1. CH4 분자 생성
atoms = build.molecule('CH4')

# 2. EMT calculator 설정
atoms.set_calculator(EMT())

# 3. 구조 최적화
optimizer = LBFGS(atoms)
optimizer.run(fmax=0.01) # fmax: 최대 힘 수렴 기준

# 4. 진동 계산
vib = Vibrations(atoms)
vib.run()

# 5. 실수 진동수 필터링 및 출력
frequencies = vib.get_frequencies() # cm^-1 단위
print("Calculated real vibrational frequencies (cm^-1):")
for freq in frequencies:
    if np.isclose(freq.imag, 0.0): # 허수부가 0에 가까운 경우만 실수 진동수로 간주
        print(f"{freq.real:.2f}")

# 진동 모드 시각화 파일 생성 (선택 사항, 주석 처리)
# vib.write_jmol()
