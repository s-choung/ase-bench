from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# N2 분자 생성
atoms = Atoms('N2', calculator=EMT())

# 진동 계산
vib = Vibrations(atoms)
vib.run()

# 진동 주파수 계산 및 출력
frequencies = vib.get_energies()
print(frequencies)
