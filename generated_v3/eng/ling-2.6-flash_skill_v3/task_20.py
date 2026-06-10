from ase.build import nanotube
from ase.io import write

cnt = nanotube((6, 6), length=4)
print(f"Number of atoms: {len(cnt)}")
print(f"Cell info: lengths={cnt.cell.lengths()}, angles={cnt.cell.angles()}")
