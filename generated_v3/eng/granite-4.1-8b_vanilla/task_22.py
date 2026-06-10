from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase import io

# Create Al(111) 3-layer slab
slab = fcc111('Al', size=(3, 1, 1), vacuum=10.0)

# Define N2 molecule
n2 = Atoms('N2')
n2.center(vacuum=5.0)

# Add N2 to the bridge site above the slab
slab = add_adsorbate(slab, n2, (0, 0, 2.0))  # height of 2.0 Å above the slab

# Set up EMT calculator
slab.calc = EMT()

# Optimize geometry (optional, but performed here for completeness)
optimizer = BFGS(slab)
optimizer.run(fmax=0.05)

# Print number of atoms and atom types in the final structure
print(f"Number of atoms: {len(slab)}")
print(f"Atom types: {[atom.symbol for atom in set(slab)]}")

# Optionally, write the structure to a file
io.write('slab_n2.traj', slab)
