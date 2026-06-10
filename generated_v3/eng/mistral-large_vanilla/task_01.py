from ase.build import bulk
from ase.calculators.emt import EMT

cu = bulk('Cu', 'fcc', a=3.6, cubic=True)
supercell = cu * (2, 2, 2)

print("Cell info:")
print(supercell.cell)
print(f"Number of atoms: {len(supercell)}")
