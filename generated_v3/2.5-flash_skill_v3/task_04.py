from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# 1. H2O 분자 생성
atoms = molecule('H2O')

# 2. EMT calculator 설정
atoms.calc = EMT()

# 3. 최적화 전 에너지 출력
initial_energy = atoms.get_potential_energy()
print(f"Initial potential energy: {initial_energy:.4f} eV")

# 4. BFGS optimizer를 사용하여 구조 최적화
optimizer = BFGS(atoms)
optimizer.run(fmax=0.01) # fmax: 최대 힘 (eV/Å)

# 5. 최적화 후 에너지 출력
final_energy = atoms.get_potential_energy()
print(f"Final potential energy: {final_energy:.4f} eV")
