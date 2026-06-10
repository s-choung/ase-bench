from ase.build import octahedron

# Cu 정팔면체 나노입자 생성
atoms = octahedron('Cu', length=5)

# 원자 수 출력
print(f"Number of atoms: {len(atoms)}")

# positions shape 출력
print(f"Positions shape: {atoms.get_positions().shape}")
