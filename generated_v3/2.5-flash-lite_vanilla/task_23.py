from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Slab 생성
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
constraint = FixAtoms(mask=[atom.tag > 0 for atom in slab])
slab.set_constraint(constraint)

# OH 분자 생성
from ase.build import molecule
oh = molecule('OH')

# 흡착 위치 및 에너지 계산
sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    slab_copy = slab.copy()
    add_adsorbate(slab_copy, oh, 1.5, site)
    slab_copy.set_calculator(EMT())
    slab_copy.get_potential_energy()
    energies[site] = slab_copy.get_potential_energy()

# 결과 출력
for site, energy in energies.items():
    print(f"{site}: {energy:.4f} eV")

min_site = min(energies, key=energies.get)
print(f"\n가장 안정한 흡착 위치: {min_site}")
