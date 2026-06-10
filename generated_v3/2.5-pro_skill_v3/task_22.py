from ase.build import fcc111, molecule, add_adsorbate

# 1. Al(111) 3층 슬래브 생성 (2x2 supercell, vacuum 10Å)
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# 2. N2 분자 생성
n2 = molecule('N2')

# 3. N2 분자를 Al(111) 슬래브의 bridge 사이트에 흡착 (높이 2.0Å)
add_adsorbate(slab, n2, height=2.0, position='bridge')

# 4. 최종 구조의 원자 수와 종류 출력
total_atoms = len(slab)
chemical_symbols = slab.get_chemical_symbols()

print(f"Total number of atoms: {total_atoms}")
print(f"Chemical symbols: {chemical_symbols}")
