from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
import numpy as np

# Pt(111) 3층 slab 생성
slab = fcc111('Pt', size=(4, 4, 3), a=3.92, vacuum=10.0)
slab.center(vacuum=10.0, axis=2)

# OH 분자 생성 (O-H 거리 약 0.96 Å)
oh_bond_length = 0.96
sites = {'ontop': (0, 0, 1.5), 'bridge': (0.5, 0.5, 1.5), 'fcc': (1/3, 1/3, 1.5)}
results = {}

for site_name, (x, y, height) in sites.items():
    atoms = slab.copy()
    
    # OH 분자 추가
    add_adsorbate(atoms, 'O', height=height, position=(x, y))
    o_index = len(atoms) - 1
    
    # H 원자 추가 (O 위에 배치)
    atoms.append('H')
    h_index = len(atoms) - 1
    atoms.positions[h_index] = atoms.positions[o_index] + np.array([0, 0, oh_bond_length])
    
    # 하단 2층 고정
    fixed_mask = atoms.positions[:, 2] < atoms.positions[:, 2].max() - 5.0
    atoms.set_constraint(FixAtoms(mask=fixed_mask))
    
    # EMT calculator 설정 및 에너지 계산
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    results[site_name] = energy
    
    print(f"{site_name:10s}: {energy:.4f} eV")

# 가장 낮은 에너지 사이트 출력
best_site = min(results, key=results.get)
print(f"\n가장 안정적인 사이트: {best_site} ({results[best_site]:.4f} eV)")
