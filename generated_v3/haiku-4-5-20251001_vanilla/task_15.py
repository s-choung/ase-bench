from ase.build import surface
from ase.calculators.emt import EMT

slab = surface('Cu', (1, 0, 0), 3, vacuum=12.0)
slab *= (3, 3, 1)

print(f"Number of atoms: {len(slab)}")
print(f"Cell parameters:\n{slab.cell}")
print(f"Cell volume: {slab.get_volume():.2f} Ų")
