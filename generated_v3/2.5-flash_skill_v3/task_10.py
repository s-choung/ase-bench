from ase.cluster import Octahedron

# Cu 정팔면체 나노입자 생성 (length=5)
atoms = Octahedron('Cu', length=5)

# 원자 수 출력
print(f"Number of atoms: {len(atoms)}")

# positions shape 출력
print(f"Positions shape: {atoms.get_positions().shape}")
