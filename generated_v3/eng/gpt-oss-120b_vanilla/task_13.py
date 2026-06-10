from ase.build import bulk
from ase.calculators.emt import EMT

# Si diamond bulk with a = 5.43 Å
si = bulk('Si', 'diamond', a=5.43)
si.set_calculator(EMT())

# 3×3×3 supercell
supercell = si * (3, 3, 3)

print("Number of atoms:", len(supercell))
print("Cell volume (Å³):", supercell.get_volume())
