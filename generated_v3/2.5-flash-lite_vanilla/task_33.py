from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# CH4 분자 생성
atoms = molecule('CH4')

# EMT 계산기 설정
atoms.calc = EMT()

# 구조 최적화
optimizer = BFGS(atoms)
optimizer.run()

# 진동 계산
vib = Vibrations(atoms)
vib.run()

# 실수 진동수만 필터링하여 출력
frequencies = vib.get_energies()
real_frequencies = [f for f in frequencies if f > 0]
print(real_frequencies)
