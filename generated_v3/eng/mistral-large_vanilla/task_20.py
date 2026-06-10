from ase.build import nanotube
from ase.calculators.emt import EMT

cnt = nanotube(6, 6, length=4)
cnt.calc = EMT()
print(f"Number of atoms: {len(cnt)}")
print("Cell info:")
print(cnt.cell)
