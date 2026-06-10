from ase import Atoms
from ase.build import fcc111, molecule, add_adsorbate, add_vacuum
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# Create Al(111) 3-layer slab
slab = fcc111('Al', size=(2, 2, 3), orthogonal=True)  # orthogonal=True for rectangular cell

# Add vacuum
add_vacuum(slab, vacuum=10.0)  # In-place modification

# Create N2 molecule
n2 = molecule('N2')

# Add adsorbate on bridge site at 2.0 Å height
add_adsorbate(slab, n2, height=2.0, position='bridge')  # In-place modification

# Set constraint (fix bottom 2 layers)
mask = [atom.index < 2*4 for atom in slab]  # 2 layers × 4 atoms per layer
slab.set_constraint(FixAtoms(mask=mask))

# Set calculator and optimize
slab.calc = EMT()
opt = BFGS(slab, trajectory='opt.traj')
opt.run(fmax=0.05)

# Print information
print(f"Number of atoms: {len(slab)}")
print("Atom types:", set(atom.symbol for atom in slab))
