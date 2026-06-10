from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# 1. N2 분자 생성
atoms = molecule('N2')

# 2. EMT calculator 설정
atoms.calc = EMT()

# 3. 구조 최적화 (진동 계산 전 필수)
optimizer = BFGS(atoms)
optimizer.run(fmax=0.01)

# 4. 진동 계산
vib = Vibrations(atoms, name='N2_vib')
vib.run()

# 5. 진동 주파수 얻기 및 출력
frequencies = vib.get_frequencies()
print("N2 vibrational frequencies (cm⁻¹):")
for freq in frequencies:
    print(f"{freq:.2f}")

# 6. 생성된 파일 정리
vib.clean()
