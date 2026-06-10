from ase.build import bulk, surface
from ase.calculators.emt import EMT

# Create Cu bulk and cut (2,1,1) surface
atoms = bulk('Cu')
slab = surface(atoms, (2, 1, 1), layers=3)

# Add vacuum
slab.center(vacuum=10.0, axis=2)

# Attach calculator
slab.calc = EMT()

print(f"Number of atoms: {len(slab)}")
print(f"Cell:\n{slab.get_cell()}")
