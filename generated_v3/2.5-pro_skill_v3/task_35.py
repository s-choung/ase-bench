import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# 1. 초기 상태와 최종 상태 정의
initial = Atoms('Al3', positions=[(0, 0, 0), (4, 0, 0), (1.5, 0.1, 0)])
initial.set_cell((10, 10, 10))
initial.pbc = True

final = initial.copy()
final.positions[2] = (2.5, -0.1, 0)

# 2. NEB 계산을 위한 이미지 생성 (총 3개)
images = [initial]
images.append(initial.copy()) # 중간 이미지 1개 추가
images.append(final)

# 3. NEB 객체 생성 및 선형 보간
neb = NEB(images)
neb.interpolate()

# 4. 중간 이미지에 Calculator 할당
for image in images[1:-1]:
    image.calc = EMT()

# 5. NEB 최적화 수행
optimizer = BFGS(neb, trajectory='Al_NEB.traj')
optimizer.run(fmax=0.05)

# 6. 각 이미지의 최종 에너지 출력
print("Final energies of the NEB path:")
# 시작점과 끝점의 에너지를 계산하기 위해 calculator 할당
initial.calc = EMT()
final.calc = EMT()
for i, atoms in enumerate(images):
    energy = atoms.get_potential_energy()
    print(f"Image {i}: {energy:.4f} eV")
