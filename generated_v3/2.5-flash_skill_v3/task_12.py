from ase.build import bulk

# Ti HCP bulk 구조 생성
# a = 2.95 Å, c/a = 1.59
atoms = bulk('Ti', 'hcp', a=2.95, c_over_a=1.59)

# Cell 벡터 출력
print("Cell vectors:")
print(atoms.get_cell())

# 원자 위치 출력
print("\nAtomic positions:")
print(atoms.get_positions())
