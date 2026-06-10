from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

# N2 분자 생성
atoms = molecule('N2')
atoms.calc = EMT()

# 구조 최적화
from ase.optimize import BFGS
dyn = BFGS(atoms)
dyn.run(fmax=0.01)

# 진동 주파수 계산
vib = Vibrations(atoms)
vib.run()
vib.summary()

# 진동 주파수 추출 (허수 주파수 제외)
frequencies = vib.get_frequencies()
frequencies = frequencies[frequencies > 0]

# 에너지 계산
energy = atoms.get_potential_energy()

# IdealGasThermo를 사용한 열역학 계산
thermo = IdealGasThermo(
    vib_energies=frequencies,
    potentialenergy=energy,
    atoms=atoms,
    geometry='linear',
    symmetrynumber=2,
    spin=0
)

# 298.15K, 1 atm에서의 열역학 성질 계산
T = 298.15
P = 101325  # Pa

G = thermo.get_gibbs_energy(temperature=T, pressure=P)
H = thermo.get_enthalpy(temperature=T)
S = thermo.get_entropy(temperature=T, pressure=P)
Cv = thermo.get_heat_capacity(temperature=T)

print(f"N2 분자 (EMT calculator)")
print(f"진동 주파수: {frequencies} cm^-1")
print(f"전자 에너지: {energy:.6f} eV")
print(f"\n298.15 K, 1 atm에서:")
print(f"Gibbs 자유에너지: {G:.6f} eV")
print(f"엔탈피: {H:.6f} eV")
print(f"엔트로피: {S:.6f} eV/K")
print(f"열용량 (Cv): {Cv:.6f} eV/K")
