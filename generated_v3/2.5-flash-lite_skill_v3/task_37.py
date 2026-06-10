from ase import Atoms, units
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# N2 분자 생성
atoms = molecule('N2')

# EMT 계산기 설정
atoms.calc = EMT()

# 구조 최적화 (진동 계산 전에 필수)
opt = BFGS(atoms)
opt.run(fmax=0.01)

# 진동 계산
vib = Vibrations(atoms, name='vib_n2')
vib.run()
vib_energies = vib.get_energies()  # 진동 에너지 (eV)

# IdealGasThermo 설정
# N2는 선형 분자이고, 대칭수는 2입니다.
thermo = IdealGasThermo(vib_energies=vib_energies, atoms=atoms,
                        geometry='linear', symmetrynumber=2, spin=0)

# Gibbs 자유에너지 계산 (298.15 K, 1 atm)
temperature = 298.15
pressure = 1 * units.atm
gibbs_energy = thermo.get_gibbs_energy(temperature=temperature, pressure=pressure)

# 결과 출력
print(f"N2 molecule vibrations calculated with EMT.")
print(f"Gibbs free energy at {temperature} K and {pressure:.2f} Pa: {gibbs_energy:.4f} eV")

# 임시 파일 정리
vib.clean()
