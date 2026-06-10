```python
from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from ase import units

# N2 분자 정의 및 EMT 계산기 설정
atoms = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)], pbc=False)
atoms.calc = EMT()

# 구조 최적화
opt = BFGS(atoms)
opt.run()

# 진동 주파수 계산
vib = Vibrations(atoms)
vib.run()
vib_energies = vib.get_energies() # eV 단위의 진동 에너지
vib_frequency_cm1 = vib.get_frequencies()[0] # cm^-1 단위의 진동 주파수

# IdealGasThermo를 사용하여 Gibbs 자유 에너지 계산
thermo = IdealGasThermo(
    vib_energies=vib_energies,
    atoms=atoms,
    geometry='linear',
    symmetrynumber=2,
    spin=0 # N2는 짝수 전자이므로 스핀은 0
)

# 298.15 K, 1 atm (101325 Pa)에서의 Gibbs 자유 에너지 계산
temperature = 298.15 # K
pressure = 1 * units.atm # Pa
gibbs_energy = thermo.get_gibbs_energy(temperature=temperature, pressure=pressure)

# 결과 출력
print(f"Optimized N-N bond length: {atoms.get_distance(0, 1):.3f} Å")
print(f"Vibrational frequency (EMT): {vib_frequency_cm1:.1f} cm^-1")
print(f"Gibbs free energy at {temperature} K, 1 atm (EMT): {gibbs_energy:.4f} eV")

# 진동 계산 파일 정리
