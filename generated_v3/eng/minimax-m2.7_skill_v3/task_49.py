import numpy as np
from ase.build import fcc111, bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Find equilibrium lattice constant via EOS
volumes, energies = [], []
a_ref = 3.6  # Cu reference lattice constant
for x in np.linspace(0.94, 1.06, 11):
    cu = bulk('Cu', 'fcc', a=a_ref * x)
    cu.calc = EMT()
    volumes.append(cu.get_volume() / 4)  # volume per atom (conventional cell has 4 atoms)
    energies.append(cu.get_potential_energy() / 4)

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = (4 * v0) ** (1/3)
print(f"Equilibrium lattice constant: {a_eq:.4f} Angstrom")

# Create fcc111 slab with 4 layers using optimized lattice constant
slab = fcc111('Cu', size=(3, 3, 4), a=a_eq, vacuum=12.0)

# Determine layer assignments based on z-coordinates
z_coords = slab.get_positions()[:, 2]
unique_z = sorted(set(z_coords))

# Fix bottom 2 layers (layers 0 and 1)
bottom_layers = unique_z[:2]
mask = np.array([any(np.isclose(z, bl) for bl in bottom_layers) for z in z_coords])
slab.set_constraint(FixAtoms(mask=mask))

# Attach EMT calculator
slab.calc = EMT()

# Run BFGS surface relaxation
opt = BFGS(slab, logfile=None)
opt.run(fmax=0.02)

# Print results
print(f"\nFinal energy: {slab.get_potential_energy():.4f} eV")
print(f"Total atoms: {len(slab)}, Fixed: {mask.sum()}, Free: {(~mask).sum()}")

# Analyze average z-coordinate per layer
final_z = slab.get_positions()[:, 2]
unique_z_final = sorted(set(final_z))

print(f"\n{'Layer':<8}{'N atoms':<10}{'Avg Z (A)':<12}{'Fixed'}")
print("-" * 42)
for i, z in enumerate(unique_z_final):
    layer_mask = np.isclose(final_z, z)
    n_atoms = layer_mask.sum()
    avg_z = final_z[layer_mask].mean()
    is_fixed = mask[layer_mask].all()
    print(f"{i+1:<8}{n_atoms:<10}{avg_z:<12.4f}{'Yes' if is_fixed else 'No'}")
