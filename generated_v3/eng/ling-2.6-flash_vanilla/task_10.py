from ase.build import fcc111, octahedron
from ase.calculics.emt import EMT

cu = octahedron('Cu', 5)
cu.calc = EMT()
print(f"Number of atoms: {len(cu)}")
print(f"Positions shape: {cu.positions.shape}")
