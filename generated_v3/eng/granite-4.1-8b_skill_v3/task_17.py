from ase import Atoms
from ase.build import surface
from ase.calculators.emt import EMT
from ase.addons import add_vacuum
from ase import units

# Create Cu bulk structure
bulk = bulk('Cu', 'fcc', a=3.6, cubic=True)

# Define Miller indices and number of layers
miller_indices = (2, 1, 1)
num_layers = 3

# Create surface using the surface function
slab = surface(bulk, miller_indices, layers=num_layers)

# Add 10 Å of vacuum in the z-direction
slab = add_vacuum(slab, vacuum=10.0, axis=2)  # axis=2 corresponds to z-direction

# Optional: Set a calculator for energy calculations (EMT in this case)
slab.calc = EMT()

# Print the number of atoms and the cell dimensions
print("Number of atoms:", len(slab))
print("Cell dimensions (Å):")
print(slab.cell)

# If you want to ensure the structure is relaxed after adding vacuum (optional)
# from ase.optimize import BFGS
# opt = BFGS(slab)
# opt.run(fmax=0.05)
