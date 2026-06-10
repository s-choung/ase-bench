from ase.build import bcc110

# Fe BCC(110) 표면 생성
# symbol='Fe', size=(2,2,4), vacuum=10 옹스트롬
atoms = bcc110(symbol='Fe', size=(2, 2, 4), vacuum=10.0)

# 원자 수 출력
print(f"원자 수: {len(atoms)}")

# cell 크기 출력
print("Cell 크기 (옹스트롬):")
print(atoms.get_cell())
