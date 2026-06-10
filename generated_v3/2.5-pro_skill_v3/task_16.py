from ase.build import bcc110

# Fe BCC(110) 표면 생성
slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

# 원자 수 출력
print(f"Number of atoms: {len(slab)}")

# Cell 크기 (a, b, c) 출력
cell_params = slab.get_cell_lengths_and_angles()
print(f"Cell dimensions (a, b, c): {cell_params[0]:.3f}, {cell_params[1]:.3f}, {cell_params[2]:.3f} Å")
