from ase import build
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase import units

# N2 분자 생성
atoms = build.molecule('N2')

# EMT calculator 설정
atoms.calc = EMT()

# 구조 최적화 (진동 계산 전 필수)
optimizer = BFGS(atoms)
optimizer.run(fmax=0.01) # 최대 힘 0.01 eV/Å 이하로 최적화

# 진동 계산
vib = Vibrations(atoms)
vib.run()

# 진동 주파수 얻기 (cm^-1 단위로 변환)
frequencies = vib.get_frequencies()

print("N2 분자의 진동 주파수 (cm^-1):")
for freq_ev in frequencies:
    # 실제 진동 모드만 출력 (허수부가 0이거나 매우 작은 경우)
    if freq_ev.imag == 0 and freq_ev.real > 0.01: # 0에 가까운 값은 무시
        print(f"{freq_ev / units.invcm:.2f}")
