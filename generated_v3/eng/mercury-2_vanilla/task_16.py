from ase.build import bulk, surface
from ase.calculators.emt import EMT

# Create BCC Fe bulk
fe_bulk = bulk('Fe', 'bcc', a=2.87)

# Generate a (110) surface slab: 4 atomic layers, 10 Å vacuum
slab = surface(fe_bulk, (1, 1, 0), layers=4, vacuum=10)

# Expand the slab to a 2×2×4 supercell
slab = slab.repeat((2, 2, 4))

# Attach a simple built‑in calculator
slab.set_calculator(EMT())

# Output information
print("Number of atoms:", len(slab))
print("Cell vectors (Å):\n", slab.get_cell())
