from ase.build import bulk

# Cu FCC bulk 생성
atoms = bulk('Cu', 'fcc', a=3.61)

# 2x2x2 supercell 생성
atoms = atoms.repeat((2, 2, 2))

# Cell 정보 출력
cell = atoms.get_cell()
print("Cell vectors:")
print(cell)
print(f"\nCell lengths and angles: {atoms.get_cell_lengths_and_angles()}")

# 원자 수 출력
print(f"\nNumber of atoms: {len(atoms)}")
