from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB
from ase.constraints import FixAtoms
from ase.io import read, write
import numpy as np

# 초기 구조 생성
slab = fcc111('Cu', size=(2, 2, 3), vacuum=10.0)
slab.calc = EMT()
slab.get_potential_energy()  # Calculator 초기화

# Cu adatom을 fcc hollow 위치에 추가
# fcc hollow 위치는 slab의 원자 위치를 기반으로 계산하거나, 경험적으로 설정할 수 있습니다.
# 여기서는 간단하게 경험적인 위치를 사용합니다.
# fcc hollow 위치는 (0.5, 0.5, z) 또는 (0.0, 0.5, z) 등 다양하게 존재합니다.
# 여기서는 (0.5, 0.5, z) 근처의 위치를 사용합니다.
initial_pos = slab.get_positions()
adatom_initial_pos = np.array([initial_pos[0, 0] + 0.5 * slab.cell[0, 0],
                               initial_pos[0, 1] + 0.5 * slab.cell[1, 1],
                               initial_pos[0, 2] + 2.0])  # 표면 위 적절한 높이

initial_atoms = slab.copy()
initial_atoms.append(initial_atoms.create_atom(symbol='Cu', position=adatom_initial_pos))

# 초기 구조 최적화 (선택 사항이지만 권장)
initial_atoms.set_constraint(FixAtoms(mask=[atom.tag < len(slab) for atom in initial_atoms]))
opt_initial = BFGS(initial_atoms, trajectory='initial_opt.traj')
opt_initial.run(fmax=0.01)

# hcp hollow 위치 추정
# hcp hollow 위치는 fcc hollow와 인접한 표면 원자들 사이의 위치입니다.
# (0.0, 0.5, z) 또는 (0.5, 0.0, z) 근처에 위치합니다.
adatom_final_pos = np.array([initial_pos[0, 0] + 0.0 * slab.cell[0, 0],
                             initial_pos[0, 1] + 0.5 * slab.cell[1, 1],
                             initial_pos[0, 2] + 2.0]) # 표면 위 적절한 높이

final_atoms = slab.copy()
final_atoms.append(final_atoms.create_atom(symbol='Cu', position=adatom_final_pos))

# 최종 구조 최적화 (선택 사항이지만 권장)
final_atoms.set_constraint(FixAtoms(mask=[atom.tag < len(slab) for atom in final_atoms]))
opt_final = BFGS(final_atoms, trajectory='final_opt.traj')
opt_final.run(fmax=0.01)

# NEB 설정
num_images = 5
images = [initial_atoms.copy() for _ in range(num_images)]

# 초기 및 최종 이미지 설정
images[0] = initial_atoms
images[-1] = final_atoms

# IDPP 보간법으로 중간 이미지 생성
neb = NEB(images)
neb.interpolate(method='idpp')

# 중간 이미지에 EMT 계산기 설정 및 고정 원자 제약 설정
for i in range(1, num_images - 1):
    images[i].calc = EMT()
    images[i].set_constraint(FixAtoms(mask=[atom.tag < len(slab) for atom in images[i]]))

# 초기 및 최종 이미지에도 EMT 계산기 설정
images[0].calc = EMT()
images[-1].calc = EMT()
images[0].set_constraint(FixAtoms(mask=[atom.tag < len(slab) for atom in images[0]]))
images[-1].set_constraint(FixAtoms(mask=[atom.tag < len(slab) for atom in images[-1]]))


# NEB 최적화 실행
optimizer = BFGS(neb, trajectory='neb.traj')
optimizer.run(fmax=0.05)

# 에너지 계산 및 에너지 장벽 출력
energies = [img.get_potential_energy() for img in images]
initial_energy = energies[0]
max_energy = np.max(energies)
energy_barrier = max_energy - initial_energy

print(f"Initial Energy: {initial_energy:.4f} eV")
print(f"Maximum Energy: {max_energy:.4f} eV")
print(f"Energy Barrier: {energy_barrier:.4f} eV")

# NEB 결과 저장 (선택 사항)
write('neb_path.traj', images)
