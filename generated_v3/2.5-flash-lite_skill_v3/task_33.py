from ase import Atoms, units
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# 1. CH4 분자 생성
atoms = molecule('CH4')

# 2. EMT 계산기 설정
atoms.calc = EMT()

# 3. 구조 최적화
opt = BFGS(atoms)
opt.run(fmax=0.01)

# 4. 진동 계산
vib = Vibrations(atoms, name='vib_ch4')
vib.run()

# 5. 실수 진동수만 필터링 및 출력
frequencies = vib.get_frequencies()
real_frequencies = frequencies[frequencies > 0]

print("Real vibrational frequencies (cm⁻¹):")
for freq in real_frequencies:
    print(f"{freq:.2f}")

vib.clean()
