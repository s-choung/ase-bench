from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# 1. H2O 분자 생성
h2o = molecule('H2O')

# 2. EMT calculator 설정
h2o.calc = EMT()

# 3. 구조 최적화 (진동 모드 계산 전 필수)
optimizer = BFGS(h2o)
optimizer.run(fmax=0.01) # 최대 힘 허용치 (eV/Å)

# 4. 진동 모드 계산
vib = Vibrations(h2o)
vib.run()

# 5. 주파수 및 에너지 추출 및 출력
frequencies_cm1 = vib.get_frequencies() # cm^-1 단위
energies_eV = vib.get_energies()        # eV 단위

print("H2O 분자의 진동 모드:")
print("----------------------")
for i, (freq, energy) in enumerate(zip(frequencies_cm1, energies_eV)):
    print(f"모드 {i+1}: 주파수 = {freq:.2f} cm^-1, 에너지 = {energy:.4f} eV")

# 6. 임시 파일 정리
vib.clean()
