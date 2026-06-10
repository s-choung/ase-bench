from ase.build import fcc100

# Cu(100) 표면 생성
# size=(x, y, layers)
# vacuum은 z 방향으로 추가되는 진공 층의 두께 (옹스트롬)
atoms = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)

# 원자 수 출력
print(f"Number of atoms: {atoms.get_global_number_of_atoms()}")

# Cell 정보 출력
print("Cell information:")
print(atoms.get_cell())
