import numpy as np
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# 1. N2 분자 구조 생성 및 최적화
atoms = molecule('N2')
atoms.center(vacuum=5.0)
atoms.calc = EMT()

optimizer = BFGS(atoms, logfile='opt.log')
optimizer.run(fmax=1e-4)

print(f"Optimized N-N bond length: {atoms.get_distance(0, 1):.4f} Å")

# 2. 진동 주파수 계산
vib = Vibrations(atoms, name='vib_N2')
vib.run()
vib_energies = vib.get_energies()

# 3. 열역학 계산 (Ideal Gas Model)
thermo = IdealGasThermo(
    vib_energies=vib_energies,
    atoms=atoms,
    geometry='linear',
    symmetrynumber=2,
    spin=0
)

# 4. 298.15 K, 1 atm 에서의 Gibbs 자유에너지 계산 및 출력
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.0)

print("\n--- Vibrational Frequencies ---")
vib.summary()

print(f"\n--- Thermochemistry ---")
print(f"Gibbs Free Energy at 298.15 K, 1 atm: {G:.4f} eV")

# 5. 계산 파일 정리
vib.clean()
