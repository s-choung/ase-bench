from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB
from ase.io import read, write
import numpy as np

# 초기 및 최종 구조 생성
# Al 원자 두 개 사이에서 세 번째 Al 원자가 이동하는 상황을 가정
initial_pos = [[0, 0, 0], [2, 0, 0], [1, 1, 0]]
final_pos = [[0, 0, 0], [2, 0, 0], [1, -1, 0]]

initial_atoms = Atoms('Al3', positions=initial_pos)
final_atoms = Atoms('Al3', positions=final_pos)

# EMT 계산기 설정
calc = EMT()
initial_atoms.calc = calc
final_atoms.calc = calc

# 초기 및 최종 구조 최적화 (선택 사항이지만 권장)
# BFGS(initial_atoms).run(fmax=0.01)
# BFGS(final_atoms).run(fmax=0.01)

# NEB 이미지 생성 (초기, 중간 3개, 최종)
n_images = 3
images = [initial_atoms] + [initial_atoms.copy() for _ in range(n_images)] + [final_atoms]

# NEB 객체 생성 및 보간
neb = NEB(images)
neb.interpolate(method='linear')

# 각 이미지에 계산기 설정 및 에너지 계산
for i, img in enumerate(images):
    img.calc = calc
    energy = img.get_potential_energy()
    print(f"Image {i} energy: {energy:.4f} eV")

# NEB 계산 실행 (선택 사항, 여기서는 에너지만 출력)
# optimizer = BFGS(neb, trajectory='neb.traj')
# optimizer.run(fmax=0.05)
