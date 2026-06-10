import numpy as np
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# 1. H2O 분자 구조 생성
h2o = molecule('H2O')

# 2. EMT 계산기 설정
h2o.calc = EMT()

# 3. 구조 최적화 (진동 계산 전 필수)
print("Optimizing H2O geometry...")
opt = BFGS(h2o, logfile=None)
opt.run(fmax=1e-4)
print("Optimization finished.")
print("-" * 30)

# 4. 진동 계산 수행
vib = Vibrations(h2o, name='vib_h2o')
vib.run()

# 5. 결과 추출 및 출력
print("H2O Vibrational Modes (EMT):")
frequencies_cm = vib.get_frequencies().real
energies_ev = vib.get_energies().real

# 3N-6 = 3개의 진동 모드만 출력 (번역/회전 모드 제외)
# EMT는 정확도가 낮아 0에 가깝지 않을 수 있으므로, 에너지가 가장 큰 3개 모드를 선택
mode_indices = np.argsort(energies_ev)[-3:]

for i in mode_indices:
    freq = frequencies_cm[i]
    energy = energies_ev[i]
    print(f"Mode {i+1}: Frequency = {freq:.2f} cm^-1, Energy = {energy:.4f} eV")

# 6. 계산 파일 정리
vib.clean()
