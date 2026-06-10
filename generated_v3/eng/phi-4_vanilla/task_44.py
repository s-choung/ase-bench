from ase.build import bulk, slab
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT

# Create a Cu(111) slab with 4 layers
slab = slab('Cu', (1, 1, 6), 4, a=3.6, vacuum=10.0, primitive=True)
slab.positions *= 1.1  # Slightly stretch to relieve periodic constraints

# Identify the bottom two layers of atoms to be fixed
nb_layers = 2
bottom_layers = slab.get_layers(zmax=slab.positions[:, 2].min() + nb_layers * slab.cell[2, 2])
fixed_indices = [atom.index for atom in slab if atom.z <= bottom_layers[-1].position[2]]

# Apply FixAtoms constraint
fixed_atoms = FixAtoms(indices=fixed_indices)
slab.set_constraint(fixed_atoms)

# Save initial coordinates of fixed atoms
initial_fixed_positions = slab.positions[fixed_indices].copy()

# Set EMT calculator
slab.set_calculator(EMT())

# Structural optimization
optimizer = BFGS(slab)
optimizer.run(fmax=0.02)

# Save final coordinates of fixed atoms
final_fixed_positions = slab.positions[fixed_indices]

# Print comparison
print("Initial coordinates of fixed atoms:")
print(initial_fixed_positions)
print("\nFinal coordinates of fixed atoms:")
print(final_fixed_positions)
