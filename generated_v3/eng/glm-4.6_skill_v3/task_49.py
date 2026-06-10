import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.eos import EquationOfState

# Find equilibrium lattice constant using EOS
print("Finding equilibrium lattice constant...")
volumes, energies = [], []
for scale in np.linspace(0.95, 1.05, 7):
    atoms = bulk('Cu', 'fcc', a=3.6*scale)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = (v0 / 4)**(1/3)
print(f"Equilibrium lattice constant: {a_eq:.4f} Å")

# Create (111) 4-layer slab
slab = fcc111('Cu', size=(2,2,4), a=a_eq, vacuum=10.0)
slab.calc = EMT()

# Fix bottom 2 layers
mask = [atom.position[2] < np.mean(slab.positions[:, 2]) for atom in slab]
bottom_layers = sorted(set([mask[i] for i in range(len(slab)) if mask[i]]))[:2]
final_mask = [mask[i] and atom.position[2] in bottom_layers for i, atom in enumerate(slab)]
slab.set_constraint(FixAtoms(mask=final_mask))

# Relax surface
BFGS(slab).run(fmax=0.01)

# Calculate layer properties
z_coords = slab.positions[:, 2]
unique_z = np.unique(np.round(z_coords, 6))
layer_z = [[] for _ in range(4)]
for atom in slab:
    layer_idx = np.argmin(np.abs(unique_z - atom.position[2]))
    layer_z[layer_idx].append(atom.position[2])

# Print results
print(f"\nFinal energy: {slab.get_potential_energy():.6f} eV")
print("Average z-coordinate for each layer:")
for i, z_list in enumerate(layer_z):
    print(f"  Layer {i+1}: {np.mean(z_list):.4f} Å")
