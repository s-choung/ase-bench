from ase.build import fcc100
from ase.calculators.emt import EMT

# Cu(100) slab, 3×3 surface, 3 layers, 12 Å vacuum
slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)
slab.calc = EMT()          # optional built‑in calculator

print("Number of atoms:", len(slab))
print("Cell (Å):")
print(slab.get_cell())
