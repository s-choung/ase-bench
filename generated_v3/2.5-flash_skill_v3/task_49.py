```python
import numpy as np
from ase import Atoms, units
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# 1. Cu FCC bulk의 격자상수를 EOS로 구하기
print("1. Cu FCC bulk 격자상수 EOS 피팅 시작...")
# 초기 Cu FCC 벌크 구조 생성 (cubic=True로 a^3 = V)
atoms_bulk = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms_bulk.calc = EMT()

cell = atoms_bulk.get_cell()
volumes = []
energies = []

# 격자상수 스케일링 범위 설정
for x in np.linspace(0.95, 1.05, 10): # 10개의 스케일링 팩터
    a = atoms_bulk.copy()
    a.set_cell(cell * x, scale_atoms=True) # 셀과 원자 위치를 함께 스케일링
    a.calc = EMT() # 각 스케일링된 구조에 계산기 재설정 (필요에 따라)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

# EOS 피팅
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# 최적 격자상수 계산 (cubic cell이므로 V = a^3)
a0 = v0**(1/3)
print(f"EOS로 구한 최적 격자상수 (a0): {a0:.4f} Å")
print(f"최적 부피 (v0): {v0:.4f} Å^3")
print(f"최적 에너지 (e0): {e0:.4f} eV")
print(f"벌크 모듈러스 (B): {B / units.GPa:.2f} GPa")
print("-" * 30)

# 2. 최적 격자상수로 (111) slab 4층 생성
print("2. (111) slab 4층 생성...")
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, a=a0) # size=(x,y,layers)
print(f"생성된 slab의 원자 수: {len(slab)}")
print("-" * 30)

# 3. slab에 EMT 계산기 설정
slab.calc = EMT()

# 4. 하부 2층 고정
# fcc111은 layer에 따라 tag를 0부터 부여 (0이 가장 아래층)
# 하부 2층은 tag가 0과 1인 원자들
mask = [atom.tag < 2 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))
print("4. 하부 2층 고정 완료.")
print("-" * 30)

# 5. BFGS로 표면 relaxation
print("5. BFGS 표면 relaxation 시작...")
optimizer = BFGS(slab, trajectory='cu_fcc111_slab_relax.traj')
optimizer.run(fmax=0.05) # fmax: eV/Å
print("표면 relaxation 완료.")
print("-" * 30)

# 6. 최종 에너지와 각 layer의 z 좌표 평균 출력
final_energy = slab.get_potential_energy()
print(f"최종 slab의 포텐셜 에너지: {final_energy:.4f} eV")

# 각 layer의 z 좌표 평균 계산
positions = slab.get_positions()
tags = slab.get_tags()

unique_tags = sorted(list(set(tags)))
print("각 layer의 z 좌표 평균:")
for tag in unique_tags:
    layer_z_coords = positions[tags == tag, 2]
    avg_z = np.mean(layer_z_coords)
    print(f"  Layer {tag}: {avg_z:.4f} Å")

print("-" *
