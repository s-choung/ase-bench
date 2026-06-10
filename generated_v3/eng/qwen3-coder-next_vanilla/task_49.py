from ase import Atoms, lattices
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.eos import EquationOfState
import numpy as np

# Equation of state to find equilibrium lattice constant
a_vals = np.linspace(3.5, 4.5, 9)
energies = []

for a in a_vals:
    bulk = lattices.fcc('Cu', a=a)
    calc = EMT()
    bulk.set_calculator(calc)
    energies.append(bulk.get_total_energy())

eos = EquationOfState(a_vals, energies)
a_eq, e0, B = eos.fit()
print(f'Equilibrium lattice constant: {a_eq:.4f} Å')

# Build (111) slab with 4 layers
layers = 4
slab = lattices.fcc111('Cu', a=a_eq, layers=layers, vacuum=10.0, periodic=True)

# Identify atomic layers based on z-coordinate
z_coords = slab.get_positions()[:, 2]
z_min = z_coords.min()
layer_thickness = a_eq / np.sqrt(6)  # Closest distance between (111) planes
layer_ids = np.floor((z_coords - z_min) / layer_thickness).astype(int)

# Fix bottom 2 layers
indices_to_fix = [i for i, layer_id in enumerate(layer_ids) if layer_id < 2]
constraint = FixAtoms(indices=indices_to_fix)
slab.set_constraint(constraint)

# Set calculator and relax
slab.set_calculator(EMT())
opt = BFGS(slab)
opt.run(fmax=0.01)

# Get final energy and average z per layer
final_energy = slab.get_total_energy()
positions = slab.get_positions()
z_coords = positions[:, 2]
layer_ids = np.floor((z_coords - z_coords.min()) / (a_eq / np.sqrt(6))).astype(int)

print(f'Final energy: {final_energy:.6f} eV')
for layer in range(layers):
    layer_indices = np.where(layer_ids == layer)[0]
    avg_z = positions[layer_indices, 2].mean()
    print(f'Layer {layer} (atoms {layer_indices}): avg z = {avg_z:.4f} Å')
