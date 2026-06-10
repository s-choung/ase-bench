```python
from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# 1. H2O 분자 초기 구조 설정
h2o = Atoms('H2O',
            positions=[(0, 0.757, 0.586),
                       (0, 0, 0),
                       (0, -0.757, 0.586)])

# 2. EMT calculator 할당
h2o.calc = EMT()

# 3. 최적화 전 에너지 계산 및 출력
initial_energy = h2o.get_potential_energy()
print(f"Initial energy: {initial_energy:.4f} eV")

# 4. BFGS optimizer를 이용한 구조 최적화 실행
optimizer = BFGS(h2o)
optimizer.run(fmax=0.05)

# 5. 최적화 후 에너지 계산 및 출력
final_energy = h2o.get_potential_energy()
print(f"Optimized energy: {final_energy:.
