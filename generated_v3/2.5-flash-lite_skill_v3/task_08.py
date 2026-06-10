from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# N2 분자 생성
atoms = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)], pbc=False)

# EMT 계산기 설정
atoms.calc = EMT()

# 구조 최적화 (진동 계산 전에 구조를 최적화하는 것이 중요)
opt = BFGS(atoms)
opt.run(fmax=0.01)

# 진동 계산 설정
vib = Vibrations(atoms, name='n2_vib')
vib.run()

# 진동 주파수 계산 및 출력
frequencies = vib.get_frequencies()
print("N2 분자의 진동 주파수 (cm⁻¹):")
for freq in frequencies:
    print(freq)

# 생성된 진동 파일 정리 (선택 사항)
vib.clean()
