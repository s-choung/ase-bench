from ase import Atoms,spm

# Create MoS2 monolayer (1x1 supercell)
mo_s2 = Atoms('MoS', positions=[(0, 0, 0), (3.1, 0, 0), (0, 2.8, 0), (3.1, 2.8, 0)],
               cell=[10, 0, 0], pbc=[1, 0, 0])  # 10Å vacuum along x-axis
mo_s2.extend(Atoms('MoS', positions=[(1.55, 1.4, 0)], cell=mo_s2.cell))

# Add 10Å vacuum in all directions
真空 = Atoms('S', positions=[(5, 5, 5)], cell=mo_s2.cell)  # Dummy atoms to extend cell
mo_s2 += 真空
cell_size = mo_s2.cell.lengths()
print(f"Cell size: {cell_size}")
