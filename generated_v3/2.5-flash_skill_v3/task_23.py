from ase import Atoms
from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.io import write

# 1. Pt(111) 3층 slab 생성
# size=(2,2,3)는 x, y 방향으로 2x2 반복, z 방향으로 3층을 의미합니다.
# vacuum=10.0은 slab 위에 10 Å의 진공 공간을 추가합니다.
base_slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# 2. OH 분자 생성
oh_molecule = molecule('OH')

# 3. 흡착 사이트 정의 및 에너지 저장 딕셔너리 초기화
adsorption_sites = ['ontop', 'bridge', 'fcc']  # 'fcc'는 fcc hollow site를 의미
energies = {}
adsorbed_structures = {}

# 4. 각 사이트에 OH 흡착 및 에너지 계산
for site in adsorption_sites:
    # 매번 새로운 slab과 OH 분자 복사본을 사용
    slab = base_slab.copy()
    oh_copy = oh_molecule.copy()

    # OH 분자를 slab에 흡착
    # height는 slab의 가장 위 원자로부터 OH 분자의 가장 아래 원자까지의 거리
    add_adsorbate(slab, oh_copy, height=1.8, position=site)

    # EMT calculator 설정
    slab.calc = EMT()

    # 단일점 에너지 계산
    energy = slab.get_potential_energy()
    energies[site] = energy
    adsorbed_structures[site] = slab

    print(f"Energy for OH on {site} site: {energy:.4f} eV")
    # 각 구조를 시각화 또는 저장하고 싶다면 아래 주석 해제
    # write(f'Pt111_OH_{site}.traj', slab)
    # write(f'Pt111_OH_{site}.xyz', slab)

# 5. 가장 낮은 에너지 사이트 비교 및 출력
min_site = min(energies, key=energies.get)
min_energy = energies[min_site]

print(f"\n--- Comparison ---")
print(f"The lowest energy site for OH adsorption is: {min_site}")
print(f"Minimum energy: {min_energy:.4f} eV")

# 가장 낮은 에너지 구조를 저장 (선택 사항)
# write('Pt111_OH_lowest_energy.traj', adsorbed_structures[min_site])
# write('Pt111_OH_lowest_energy.xyz', adsorbed_structures[min_site])
