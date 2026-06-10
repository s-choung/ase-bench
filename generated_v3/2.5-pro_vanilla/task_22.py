from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT

# 1. Al(111) 슬랩 생성 (3층)
slab = fcc111('Al', size=(2, 2, 3), orthogonal=True, vacuum=None)

# 2. N2 분자 생성
n2 = molecule('N2')

# 3. 슬랩의 bridge 사이트에 N2 분자 흡착
add_adsorbate(slab, n2, height=2.0, position='bridge')

# 4. z축 방향으로 10 옹스트롬의 진공층 추가
slab.center(vacuum=10.0, axis=2)

# 5. ASE 내장 계산기 설정 (선택 사항)
slab.calc = EMT()

# 6. 최종 구조의 원자 수와 종류 출력
total_atoms = len(slab)
atomic_species = sorted(list(set(slab.get_chemical_symbols())))

print(f"Total number of atoms: {total_atoms}")
print(f"Atomic species: {atomic_species}")
