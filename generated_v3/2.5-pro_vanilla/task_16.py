from ase.build import bcc110

# Fe BCC(110) 표면 생성: size=(2,2,4), vacuum=10.0 Angstrom
surface = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

# 원자 수 출력
print(f"Total number of atoms: {len(surface)}")

# Cell 크기 (벡터) 출력
print("Cell dimensions (vectors):")
print(surface.cell)
