import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# 1. 시스템 설정
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# 2. 진동 계산 수행
# 각 원자를 x, y, z 방향으로 0.01 Å 씩 이동시켜 힘을 계산
vib = Vibrations(atoms, name="vib_cu", delta=0.01)
vib.run()

# 3. 열역학적 특성 계산
# 계산된 진동 모드의 에너지 (hbar * omega)를 가져옴
vib_energies = vib.get_energies()

# HarmonicThermo를 사용하여 Helmholtz 자유에너지 계산
thermo = HarmonicThermo(vib_energies=vib_energies)
helmholtz_energy = thermo.get_helmholtz_energy(temperature=300)

# 4. 결과 출력
print(f"Vibrational modes (meV):")
for energy in vib.get_energies():
    if np.iscomplex(energy):
        print(f"  - (imaginary mode)")
    else:
        print(f"  - {energy * 1000:.2f}")

print("\n" + "="*40)
print(f"Helmholtz free energy at 300 K: {helmholtz_energy:.4f} eV")
print("="*40)

# 계산 파일 정리
vib.clean()
