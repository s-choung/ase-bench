from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
import numpy as np

# 1. Cu bulk 생성 및 구조 최적화
a = 3.61  # Cu lattice constant (approximate)
atoms = bulk('Cu', 'fcc', a=a)
atoms.calc = EMT()
opt = BFGS(atoms)
opt.run(fmax=0.01)

# 2. 진동 주파수 계산
vib = Vibrations(atoms, name='cu_vib')
vib.run()
freqs_cm_inv = vib.get_frequencies()  # Frequencies in cm^-1

# 3. HarmonicThermo를 사용한 Helmholtz 자유 에너지 계산
# HarmonicThermo는 진동 모드 에너지(vib_energies)를 필요로 합니다.
# 진동 모드 에너지는 주파수(cm^-1)로부터 계산됩니다.
# eV 단위로 변환하여 사용합니다.
vib_energies_ev = freqs_cm_inv * units.invcm / units.Hartree  # Convert cm^-1 to eV

# HarmonicThermo 객체 생성
# geometry, symmetrynumber, spin은 분자 특성에 따라 달라지며, 벌크 결정에서는 일반적으로 사용되지 않거나 기본값을 사용합니다.
# 여기서는 벌크 결정이므로, atoms 객체만 전달합니다.
thermo = HarmonicThermo(vib_energies=vib_energies_ev, atoms=atoms)

# 300K에서의 Helmholtz 자유 에너지 계산 (eV 단위)
# Helmholtz 자유 에너지 (A) = E_electronic + E_vibrational - TS
# HarmonicThermo의 get_helmholtz_free_energy 함수는 eV 단위로 반환합니다.
temperature = 300.0  # Kelvin
helmholtz_free_energy_ev = thermo.get_helmholtz_free_energy(temperature=temperature)

# 결과 출력
print(f"Cu bulk (EMT calculator) vibrational frequencies (cm^-1): {freqs_cm_inv}")
print(f"Cu bulk (EMT calculator) Helmholtz free energy at {temperature} K (eV): {helmholtz_free_energy_ev}")
