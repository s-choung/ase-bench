from ase.build import surface
from ase.calculators.emt import EMT

# Create Cu(100) surface
# size=(3,3,3) refers to the repetitions in x, y, and z
# vacuum is added to the z-axis
slab = surface('Cu', (1, 0, 0), layers=3, size=(3, 3, 1), vacuum=12.0)

# Set calculator
slab.calc = EMT()

print(f"Number of atoms: {len(slab)}")
print(f"Cell vectors:\n{slab.get_cell()}")
