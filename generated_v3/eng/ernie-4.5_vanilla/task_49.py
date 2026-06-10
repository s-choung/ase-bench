from ase.build import fcc111, bulk
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.io import write
import numpy as np

# Step 1: Find the equilibrium lattice constant for Cu FCC using EMT and Equation of States (EOS)
a_range = np.linspace(3.4, 4.0, 10)
energies = []

for a in a_range:
    atoms = bulk('Cu', 'fcc', latticeconstant=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())

# Fit to an equation of state (quadratic for simplicity)
fit = np.polyfit(a_range, energies, 2)
a0 = -fit[1] / (2 * fit[0])  # top of the parabola

# Step 2: Create a 4-layer (111) slab
slab = fcc111('Cu', size=(1, 1, 4), a=a0, vacuum=10.0)

# Step 3: Attach EMT calculator
slab.calc = EMT()

# Step 4: Fix the bottom 2 layers
constraints = FixAtoms(mask=[z < a0 * 2 for z in slab.positions[:, 2]])
slab.set_constraint(constraints)

# Step 5: Run BFGS surface relaxation
optimizer = BFGS(slab, trajectory='relax.traj')
optimizer.run(fmax=0.01)

# Step 6: Print final energy and average z-coordinate for each layer
final_energy = slab.get_potential_energy()
print(f"Final energy: {final_energy:.4f} eV")

layers = {}
for atom in slab:
    z = atom.position[2]
    layer_index = int(z // (a0 / 2))  # Divide into 4 layers vertically
    if layer_index not in layers:
        layers[layer_index] = []
    layers[layer_index].append(z)

for layer_index, z_coords in layers.items():
    avg_z = sum(z_coords) / len(z_coords)
    print(f"Layer {layer_index + 1} average z-coordinate: {avg_z:.4f} Å")
