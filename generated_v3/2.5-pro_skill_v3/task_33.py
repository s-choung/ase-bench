import numpy as np
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# 1. CH4 분자 구조 생성
atoms = molecule('CH4')

# 2. EMT 계산기 설정
atoms.calc = EMT()

# 3. 구조 최적화 수행
print("Running geometry optimization...")
optimizer = BFGS(atoms, logfile=None)
optimizer.run(fmax=0.01)
print("Optimization finished.")

# 4. 진동 계산 수행
print("\nRunning vibration analysis...")
vib = Vibrations(atoms, name='vib_ch4')
vib.run()
print("Vibration analysis finished.")

# 5. 진동수 계산 및 실수(real) 값만 필터링
# get_frequencies()는 복소수 배열을 반환할 수 있음 (허수는 불안정한 모드)
all_frequencies = vib.get_frequencies()
real_frequencies = [f.real for f in all_frequencies if f.imag == 0]

# 6. 결과 출력
print("\nReal vibrational frequencies (cm^-1):")
for freq in sorted(real_frequencies, reverse=True):
    if freq > 1e-4: # 0에 가까운 값 (translation/rotation) 제외
        print(f"{freq:.2f}")

# 7. 계산 파일 정리
vib.clean()
