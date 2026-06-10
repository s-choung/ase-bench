from ase.build import nanotube

# (6,6) carbon nanotube 생성, length=4
atoms = nanotube(6, 6, length=4)

# 원자 수 출력
print(f"Number of atoms: {len(atoms)}")

# Cell 정보 출력
print("Cell information:")
print(atoms.get_cell())
