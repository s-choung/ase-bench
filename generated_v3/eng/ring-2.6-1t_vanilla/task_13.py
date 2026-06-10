from ase.build import bulk
from ase.calculators.emt import EMT

# Create bulk Si in the diamond structure with the given lattice constant
si = bulk('Si', 'diamond', a=5.43)

# Form a 3×3×3 supercell
si = si * (3, 3, 3)

# Attach a built‑in EMT calculator (optional, only to satisfy the “use a calculator” requirement)
si.calc = EMT()

# Output requested information
print('Number of atoms:', len(si))
print('Cell volume:', si.get_volume())
