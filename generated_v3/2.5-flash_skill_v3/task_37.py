from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from ase import units

# 1. N2 분자 생성
atoms = molecule('N2')

# 2. EMT 계산기 설정
atoms.calc = EMT()

# 3. 구조 최적화 (진동 계산 전 필수)
optimizer = BFGS(atoms)
optimizer.run(fmax=0.01)

# 4. 진동 주파수 계산
vib = Vibrations(atoms)
vib.run()
vib_energies = vib.get_energies() # eV 단위의 진동 에너지

# 5. IdealGasThermo를 사용하여 Gibbs 자유 에너지 계산
temperature = 298.15 # K
pressure = 1 * units.atm # 1 atm을 Pa 단위로 변환

thermo = IdealGasThermo(
    vib_energies=vib_energies,
    atoms=atoms,
    geometry='linear',
    symmetrynumber=2,
    spin=0 # N2는 스핀 0 (싱글렛)
)

gibbs_energy = thermo.get_gibbs_energy(temperature=temperature, pressure=pressure)

# 6. 결과 출력
print(f"N2 분자의 298.15K, 1 atm에서의 Gibbs 자유 에너지: {gibbs_energy:.4f} eV")

# 진동 계산 파일 정리
vib.clean()
