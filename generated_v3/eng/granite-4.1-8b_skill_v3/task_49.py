from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.lattice.surface import fcc111
from ase.optimize import BFGS
from ase.io import write
from ase.thermochemistry import EquationOfState
from ase import units
import numpy as np

# EOS fitting for Cu FCC bulk
# Prepare volumes and energies
volumes = []
energies = []
a_vals = np.linspace(3.49, 3.53, 7)  # FCC Cu lattice constant range
for a in a_vals:
    atoms_bulk = Atoms('Cu', cell=[a, a, a], pbc=True, cellpar=[a, a, a, 90, 90, 90])
    atoms_bulk.calc = EMT()
    energy = atoms_bulk.get_potential_energy()
    volumes.append(atoms_bulk.get_volume())
    energies.append(energy)

# Fit Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = np.cbrt(v0)  # lattice constant from volume

print(f'Equilibrium lattice constant: {a_eq:.3f} Å')

# Create (111) 4-layer slab with equilibrium lattice constant
slab = fcc111('Cu', size=(2, 2, 4), a=a_eq, vacuum=10.0)
# Fix bottom 2 layers
mask = [atom.tag >= 4 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

# Run surface relaxation
slab.calc = EMT()
relaxer = BFGS(slab)
relaxer.run(fmax=0.05)

# Output final energy and average z-coordinate for each layer
final_energy = slab.get_potential_energy()
z_coords = slab.get_positions()[:, 2]
layer_z = np.array_split(z_coords, 4)  # split into 4 layers
avg_z_per_layer = [np.mean(layer) for layer in layer_z]

print(f'Final energy: {final_energy:.6f} eV')
for i, avg_z in enumerate(avg_z_per_layer, start=1):
    print(f'Average z-coordinate of layer {i}: {avg_z:.6f} Å')

# Optional: write relaxed slab to file for visualization
write('relaxed_slab.xyz', slab)
