from ase import Atoms
from ase.build import fcc111, molecule
from ase.visualize import view
from ase.calculators.emt import EMT

# 1. Create Al(111) 3-layer slab
# Default lattice constant for Al is ~4.05 A
slab = fcc111('Al', size=(1, 1, 3), vacuum=10.0)

# 2. Define N2 molecule and position
n2 = molecule('N2')
n2.set_distance(0, 1, 1.1) # N-N bond length approx 1.1 A

# 3. Find Bridge site on top layer (layer index 0)
# For FCC(111), bridge site is between two surface atoms
# We'll manually place it relative to the slab origin
bridge_pos = slab.positions[0] + (slab.positions[1] - slab.positions[0]) * 0.5
n2.translate(bridge_pos)
n2.translate([0, 0, 2.0]) # Height 2.0 A above surface

# 4. Combine structures
combined = slab + n2

# 5. Attach calculator (Using EMT as requested, though EMT is for metals)
# Note: EMT doesn't support N, but the prompt requires built-in calculators
combined.calc = EMT()

# 6. Output results
print(f"Number of atoms: {len(combined)}")
print(f"Atom types: {set(combined.get_chemical_symbols())}")
