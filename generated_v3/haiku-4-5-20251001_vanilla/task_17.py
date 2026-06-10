from ase.build import surface
from ase.calculators.emt import EMT

slab = surface('Cu', (2, 1, 1), 3, vacuum=10.0)
slab.calc = EMT()

print(f"Number of atoms: {len(slab)}")
print(f"Cell parameters:\n{slab.cell}")
print(f"Cell volume: {slab.get_volume():.2f} Ų")
