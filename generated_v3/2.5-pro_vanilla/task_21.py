from ase.cluster import Icosahedron

# Au Icosahedron 나노입자 생성 (noshells=3)
atoms = Icosahedron('Au', noshells=3)

# 원자 수 출력
num_atoms = len(atoms)
print(f"Number of atoms: {num_atoms}")

# 질량 중심(center of mass) 출력
com = atoms.get_center_of_mass()
print(f"Center of mass: {com}")
