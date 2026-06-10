from ase.build import bulk

# 1. Cu FCC bulk 생성
# Cu의 격자 상수 (a)는 약 3.6Å
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)

# 2. 2x2x2 supercell 생성
supercell_atoms = atoms * (2, 2, 2)

# 3. supercell 정보 출력
print("Supercell Cell (3x3 matrix):\n", supercell_atoms.get_cell())
print("Number of atoms in supercell:", supercell_atoms.get_number_of_atoms())
