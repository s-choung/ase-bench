from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.geometry import get_distances
from ase import Atoms
from scipy.optimize import curve_fit
import numpy as np

# Volume as function of lattice constant
def get_volume(a, c):
    return a**2 * c

# Equation of State (EOS) - Birch-Murnaghan
def birch_murnaghan(V, E0, B0, BP, V0):
    eta = (V0 / V)**(2/3)
    return E0 + (9 * V0 * B0 / 16) * ((eta - 1)**3 * BP + (eta - 1)**2 * (6 - 4 * eta))

# Find equilibrium lattice constant
lattice_constants = np.linspace(3.75, 4.25, 20)
energies = []
volumes = []

for a in lattice_constants:
    bulk_metal = bulk('Cu', 'fcc', a=a)
    calc = EMT()
    bulk_metal.set_calculator(calc)
    energies.append(bulk_metal.get_potential_energy())
    volumes.append(get_volume(a, a))

params, _ = curve_fit(birch_murnaghan, volumes, energies, p0=[-1.0, 0.0, 4.0, 40.0])
E0, B0, BP, V0 = params
equilibrium_a = a * (V0 / get_volume(equilibrium_a, equilibrium_a))**(1/3)

# Create a (111) surface
slab = fcc111('Cu', size=(4, 4, 4), vacuum=10.0, a=equilibrium_a)
calc = EMT()
slab.set_calculator(calc)

# Fix the bottom two layers
fixed_indices = slab.get_layers(distance=0, positions='z')[:2]
slab.set_constraint(FixAtoms(indices=fixed_indices))

# Run BFGS surface relaxation
relaxation = BFGS(slab)
relaxation.run(fmax=0.01)

# Calculate final energy and average z-coordinate for each layer
z_coords = slab.positions[:, 2]
min_z = z_coords.min()
layer_spacings = [(min_z + i * slab.get_cell()[2, 2]) for i in range(4)]

average_z = np.zeros(4)
for i in range(4):
    lower_bound = layer_spacings[i] if i == 0 else layer_spacings[i] - 0.1
    upper_bound = layer_spacings[i + 1] if i < 3 else min_z + 1.0
    mask = (z_coords >= lower_bound) & (z_coords < upper_bound)
    average_z[i] = z_coords[mask].mean()

print(f"Final Energy: {slab.get_potential_energy():.3f} eV")
print("Average z-coordinates for each layer:")
for i, z in enumerate(average_z, start=1):
    print(f"Layer {i}: {z:.3f} Angstrom")
