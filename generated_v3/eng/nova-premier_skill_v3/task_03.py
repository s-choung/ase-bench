from ase.build import mx2
from ase.io import write

mos2 = mx2('MoS2', kind='2H', thickness=3.15, orthogonal=True)
add_vacuum(mos2, 10)
cell = mos2.get_cell_lengths_and_angles()
print("Cell:", [f"{x:.2f}" for x in cell])
