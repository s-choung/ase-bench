from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Cu bulk 생성
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)

# EMT calculator 설정
atoms.calc = EMT()

# 진동 계산
vib = Vibrations(atoms)
vib.run()

# HarmonicThermo 객체 생성
harmonic_thermo = HarmonicThermo(vib.get_hessian())

# 300K에서의 Helmholtz 자유 에너지 계산 (eV 단위)
free_energy = harmonic_thermo.get_free_energy(atoms, temperature=300)

# 결과 출력
print(f"Helmholtz free energy at 300K: {free_energy:.4f} eV")
