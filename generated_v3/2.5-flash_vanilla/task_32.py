from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# H2O 분자 생성
atoms = molecule('H2O')

# EMT calculator 설정
atoms.set_calculator(EMT())

# 구조 최적화
dyn = BFGS(atoms)
dyn.run(fmax=0.01) # fmax를 낮춰 더 정밀하게 최적화

# 진동 모드 계산
vib = Vibrations(atoms)
vib.run()

# 결과 출력
print("H2O 분자의 진동 모드:")
energies = vib.get_energies()
frequencies_thz = vib.get_frequencies()

# THz를 cm^-1로 변환하는 상수
THZ_TO_CM_1 = 33.35641

for i, (energy_ev, freq_thz) in enumerate(zip(energies, frequencies_thz)):
    # 허수 주파수 (음수 에너지)는 불안정한 모드를 나타냄
    if energy_ev.imag != 0:
        print(f"Mode {i+1}: Imaginary Frequency = {freq_thz.imag:.2f} THz (Unstable mode)")
    else:
        freq_cm_1 = freq_thz.real * THZ_TO_CM_1
        print(f"Mode {i+1}: Frequency = {freq_cm_1:.2f} cm^-1, Energy = {energy_ev.real:.4f} eV")

# 진동 모드 시각화 파일 생성 (선택 사항, 주석 처리)
# vib.write_jmol()
