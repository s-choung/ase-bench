from ase.cluster import Octahedron

# Cu 정팔면체 나노입자 생성 (length=5)
nanoparticle = Octahedron('Cu', length=5, latticeconstant=3.61)

# 원자 수와 positions shape 출력
print(f"Number of atoms: {len(nanoparticle)}")
print(f"Positions shape: {nanoparticle.positions.shape}")
