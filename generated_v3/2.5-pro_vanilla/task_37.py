import numpy as np
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# 1. N2 분자 구조 생성 및 최적화
n2 = molecule('N2')
n2.calc = EMT()
optimizer = BFGS(n2)
optimizer.run(fmax=0.01)

# 2. 진동 주파수 계산
vib = Vibrations(n2)
vib.run()
vib_energies = vib.get_energies()

# 3. 열화학 계산 (Gibbs 자유에너지)
potential_energy = n2.get_potential_energy()

thermo = IdealGasThermo(
    vib_energies=vib_energies,
    potentialenergy=potential_energy,
    atoms=n2,
    geometry='linear',
    symmetrynumber=2,
    spin=0)

G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.)

# 4. 결과 출력
print(f"Vibrational energies (eV): {np.real(vib_energies)}")
print(f"Gibbs Free Energy at 298.15 K, 1 atm: {G:.4f} eV")
