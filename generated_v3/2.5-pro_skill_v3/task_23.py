import numpy as np
from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

# 1. Pt(111) 슬래브와 OH 흡착물 생성
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0, orthogonal=True)
oh = Atoms('OH', positions=[(0, 0, 0), (0, 0, 0.97)])
adsorption_height = 1.9

# 2. 각 흡착 사이트에 대한 구조 생성 및 에너지 계산
sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    system = slab.copy()
    add_adsorbate(system, oh, height=adsorption_height, position=site)
    
    system.calc = EMT()
    energy = system.get_potential_energy()
    energies[site] = energy

# 3. 결과 출력 및 가장 안정한 사이트 비교
print("Adsorption energies for OH on Pt(111):")
for site, energy in energies.items():
    print(f"  - {site:<10}: {energy:.4f} eV")

stable_site = min(energies, key=energies.get)
min_energy = energies[stable_site]

print(f"\nMost stable site: '{stable_site}' ({min_energy:.4f} eV)")
