from ase.build import fcc111, add_vacuum
from ase.io import write
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# Pt(111) 4층 slab 생성
slab = fcc111('Pt', size=(4, 4, 4), a=3.92, vacuum=10.0)

# CO 분자 생성
from ase.build import molecule
co = molecule('CO')

# CO를 ontop 사이트에 배치
# ontop 사이트는 상단 Pt 원자 위
co.translate([slab.cell[0, 0]/2, slab.cell[1, 1]/2, slab.get_positions()[:, 2].max() + 2.5])

# slab과 CO 결합
from ase.build import add_adsorbate
slab_with_co = slab.copy()
slab_with_co += co

# 하단 2층 고정
z_positions = slab_with_co.get_positions()[:, 2]
z_unique = sorted(set(z_positions))
fixed_z = z_unique[:2]
constraint = FixAtoms(mask=[z < max(fixed_z) + 0.1 for z in z_positions])
slab_with_co.set_constraint(constraint)

# EMT calculator 설정 및 구조 최적화
slab_with_co.calc = EMT()
dyn = BFGS(slab_with_co, trajectory='co_ontop.traj')
dyn.run(fmax=0.05, steps=100)

# 최종 원자 수 출력
print(f"Total number of atoms: {len(slab_with_co)}")
