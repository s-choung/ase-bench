from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize.neb import NEB
from ase.constraints import FixAtoms
from ase.io import Trajectory
import numpy as np

# 초기 및 최종 구조 생성
slab = fcc111('Cu', size=(2, 2, 2), vacuum=10.0)
slab.calc = EMT()
initial_pos = slab.get_positions()

# adatom 생성 및 slab 위에 배치 (fcc hollow)
adatom = bulk('Cu', 'fcc', a=3.61)
adatom.translate([1.29, 1.29, 2.0]) # fcc hollow 위치 근사
initial_images = [slab.copy() for _ in range(5)]
initial_images[0].extend(adatom)
initial_images[0].positions[-1, :] = initial_pos[0] + [1.29, 1.29, 2.0] # fcc hollow 위치

# hcp hollow 위치로 adatom 이동 (근사)
final_images = [slab.copy() for _ in range(5)]
final_images[-1].extend(adatom)
final_images[-1].positions[-1, :] = initial_pos[0] + [2.58, 0.0, 2.0] # hcp hollow 위치 근사

# NEB 계산 설정
neb = NEB(initial_images,
          calculator=EMT(),
          interpolation='idpp',
          k=0.1) # k 값은 필요에 따라 조정

# 고정 원자 설정 (slab의 하부 층)
for img in neb.images:
    constraint = FixAtoms(indices=[atom.index for atom in img if atom.position[2] < 3.0])
    img.set_constraint(constraint)

# NEB 최적화
neb.interpolate()
neb.optimize()

# 결과 분석
energies = [img.get_potential_energy() for img in neb.images]
max_energy = np.max(energies)
initial_energy = energies[0]
energy_barrier = max_energy - initial_energy

print(f"Energy barrier: {energy_barrier:.4f} eV")

# Trajectory 저장 (선택 사항)
traj = Trajectory('neb_cu_adatom.traj', 'w')
for img in neb.images:
    traj.write(img)
traj.close()
