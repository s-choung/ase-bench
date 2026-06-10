```python
import numpy as np
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS

# 1. 시스템 설정
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, orthogonal=True)
adsorbate = 'Cu'
height = 1.8

# 2. 초기 및 최종 상태 생성
initial = slab.copy()
add_adsorbate(initial, adsorbate, height, position='fcc')

final = slab.copy()
add_adsorbate(final, adsorbate, height, position='hcp')

# 3. 제약 조건 설정 (아래 2개 층 고정)
constraint = FixAtoms(mask=[atom.tag < 3 for atom in initial])
calc = EMT()

# 4. NEB 이미지 생성 및 설정
images = [initial] + [initial.copy() for _ in range(5)] + [final]
for image in images:
    image.calc = calc
    image.set_constraint(constraint)

# 5. NEB 객체 생성 및 보간
neb = NEB(images, allow_climb=True)
neb.interpolate(method='idpp')

# 6. NEB 계산 실행
optimizer = BFGS(neb, trajectory='Cu_fcc_hcp.traj')
optimizer.run(fmax=0.05)

# 7. 결과 분석 및 출력
energies = [image.get_potential_energy() for image in images]
initial_energy = energies[0]
barrier_energy = max(energies)
activation_energy = barrier_energy - initial_energy

print(f"Initial Energy: {initial_energy:.3f} eV")
print(f"Highest Energy on Path: {barrier_energy:.3f} eV")
print(f"Energy Barrier (fcc ->
