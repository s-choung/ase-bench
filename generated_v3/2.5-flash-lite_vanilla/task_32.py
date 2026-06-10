from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# H2O 분자 생성
atoms = molecule('H2O')

# EMT calculator 설정
atoms.calc = EMT()

# 진동 계산 객체 생성
vib = Vibrations(atoms)
vib.run()

# 각 진동 모드의 주파수와 에너지 계산 및 출력
for i in range(len(vib.get_energies())):
    freq = vib.get_frequencies()[i]
    energy = vib.get_energies()[i]
    print(f"Mode {i+1}: Frequency = {freq:.2f} cm^-1, Energy = {energy:.4f} eV")
