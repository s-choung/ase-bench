from ase import Atoms
from ase.build import bulk, fcc111, add_adsorbate, fix_atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

# Create a Cu(111) 4-layer slab
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True, orthorhombic=True)
atoms = atoms[:4]  # Keep only the top 4 layers
atoms.cell *= 3.6

# Add CO molecule as an adsorbate
co = Atoms({'C': 1, 'O': 1}, positions=[[0, 0, 2.0], [1, 0, 2.0]], size=(1, 1))
add_adsorbate(atoms, co, height=1.8, position='ontop')

# Fix the bottom 2 layers to avoid relaxing them
fixed_layers = fix_atoms(atoms, mask=[a.tag < 2 for a in atoms])
atoms.set_constraint(fixed_layers)

# Calculate the initial structure with EMT
atoms.calc = EMT()

# Optimize the structure with BFGS
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Print the coordinates of the fixed atoms before and after optimization
print("Fixed Atoms Before Optimization:")
for atom in atoms[:2]:
    print(atom.position)

print("\nFixed Atoms After Optimization:")
for atom in atoms[:2]:
    print(atom.position)

# Check if the fixed atoms have moved
moved = any(np.linalg.norm(atom.position - prev_position) > 1e-6 for atom, prev_position in zip(atoms[:2], [atom.position for atom in atoms[:2]]))
if moved:
    print("\nWARNING: Fixed atoms have moved during optimization!")
else:
    print("\nFixed atoms have remained fixed during optimization.")
