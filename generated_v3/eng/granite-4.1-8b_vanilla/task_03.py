from ase import Atoms
from ase.build import mx2
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vacuum import add_vacuum_layer
from ase.io import write

# Create MoS2 monolayer
structure = mx2(formula='MoS2', kind='MoS2', a=3.18, thickness=0.6)

# Add vacuum layer
structure = add_vacuum_layer(structure, vacuum=10)

# Print cell size
print("Cell size:", structure.cell)

# Optional: Relax the structure (not required for the task, but demonstrates usage)
structure.calc = EMT()
relax = BFGS(structure, trajectory=None)
relax.run(fmax=0.05)

# Write to file for verification (optional)
# write('mos2_monolayer.ext', structure)
