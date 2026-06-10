from ase.build import bulk

# Diamond Si bulk 생성
atoms = bulk('Si', 'diamond', a=5.43)

# 3x3x3 supercell 생성
atoms = atoms.repeat((3, 3, 3))

# 원자 수와 cell volume 출력
print(f"Number of atoms: {len(atoms)}")
print(f"Cell volume: {atoms.get_volume():.2f} Ų")
