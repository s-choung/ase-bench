from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.io import read, write

# Pt(111) 3층 slab 생성
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
# slab의 하부 2개 층 고정
constraint = FixAtoms(mask=[atom.tag > 1 for atom in slab])
slab.set_constraint(constraint)

# OH 분자 생성
oh = molecule('OH')

# 흡착 사이트 정의
sites = ['ontop', 'bridge', 'fcc']
energies = {}

# 각 사이트에 흡착 및 계산
for site in sites:
    slab_copy = slab.copy()
    # 흡착 높이는 대략적인 값으로 설정 (실제로는 최적화 필요)
    if site == 'ontop':
        height = 1.8
    elif site == 'bridge':
        height = 1.5
    elif site == 'fcc':
        height = 1.6
    else:
        height = 1.8 # default

    add_adsorbate(slab_copy, oh, height, position=site)

    # 구조 최적화 (선택 사항이지만, 더 정확한 비교를 위해 포함)
    slab_copy.calc = EMT()
    opt = BFGS(slab_copy, trajectory=f'{site}_opt.traj')
    opt.run(fmax=0.05)

    # Single-point 에너지 계산
    slab_copy.calc = EMT()
    energy = slab_copy.get_potential_energy()
    energies[site] = energy
    print(f"{site} site energy: {energy:.4f} eV")

# 가장 낮은 에너지 사이트 찾기
min_site = min(energies, key=energies.get)
print(f"\nLowest energy site: {min_site} ({energies[min_site]:.4f} eV)")

# 각 구조 저장 (선택 사항)
for site, energy in energies.items():
    slab_copy = slab.copy()
    if site == 'ontop':
        height = 1.8
    elif site == 'bridge':
        height = 1.5
    elif site == 'fcc':
        height = 1.6
    else:
        height = 1.8

    add_adsorbate(slab_copy, oh, height, position=site)
    slab_copy.calc = EMT()
    opt = BFGS(slab_copy, trajectory=f'{site}_opt.traj')
    opt.run(fmax=0.05)
    write(f'{site}_adsorbed.xyz', slab_copy)
