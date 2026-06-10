from ase.build import bulk, make_supercell

# Cu FCC bulk 생성
atoms = bulk('Cu', 'fcc', a=3.6)

# 2x2x2 supercell 생성
P = [[2, 0, 0],
     [0, 2, 0],
     [0, 0, 2]]
supercell_atoms = make_supercell(atoms, P)

# Cell 정보 출력
print("Supercell Cell:", supercell_atoms.get_cell())

# 원자 수 출력
print("Number of atoms in supercell:", len(supercell_atoms))
