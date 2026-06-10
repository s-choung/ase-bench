from ase.build import fcc111, molecule, add_adsorbate

# Al(111) slab 생성 (3층, 10 옹스트롬 진공)
# Al의 격자 상수 (a)는 일반적인 값을 사용합니다.
al_slab = fcc111('Al', size=(2, 2, 3), a=4.05, vacuum=10.0)

# N2 분자 생성
n2_molecule = molecule('N2')

# N2 분자를 Al(111) slab의 bridge 사이트에 2.0 옹스트롬 높이로 흡착
# add_adsorbate 함수는 첫 번째 인자인 slab 객체를 직접 수정합니다.
add_adsorbate(al_slab, n2_molecule, height=2.0, position='bridge')

# 최종 구조의 원자 수와 원자 종류 출력
print(f"Total number of atoms: {len(al_slab)}")
print(f"Atom types: {sorted(list(set(al_slab.get_chemical_symbols())))}")
