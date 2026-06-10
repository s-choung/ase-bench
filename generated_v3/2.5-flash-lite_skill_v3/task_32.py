from ase import Atoms, units
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# H2O 분자 생성
atoms = molecule('H2O')

# EMT 계산기 설정
atoms.calc = EMT()

# 구조 최적화 (진동 계산 전에 구조를 최적화하는 것이 일반적입니다)
from ase.optimize import BFGS
optimizer = BFGS(atoms)
optimizer.run(fmax=0.01)

# 진동 계산 설정
vib = Vibrations(atoms, name='h2o_vib')
vib.run()

# 각 진동 모드의 주파수와 에너지 출력
frequencies = vib.get_frequencies()  # cm^-1 단위
energies = vib.get_energies()      # eV 단위

print("H2O 진동 모드:")
for i, (freq, energy) in enumerate(zip(frequencies, energies)):
    print(f"모드 {i+1}: 주파수 = {freq:.2f} cm⁻¹, 에너지 = {energy:.4f} eV")

vib.clean()
