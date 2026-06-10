from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# Calculate equilibrium lattice constant via equation of state
a_scan = np.linspace(3.5, 3.7, 10)
volumes, energies = [], []
for a in a_scan:
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())
eos = EquationOfState(volumes, energies)
v0, _, _ = eos.fit()
a0 = v0 ** (1/3)

# Create 4-layer Cu(111) slab with calculated lattice constant
slab = fcc111('Cu', size=(3, 3, 4), a=a0, vacuum=10.0)
slab.calc = EMT()

# Fix bottom two layers
z_coords = slab.positions[:, 2]
z_min, z_max = z_coords.min(), z_coords.max()
fix_mask = z_coords < z_min + 2*(z_max - z_min)/4
slab.set_constraint(FixAtoms(mask=fix_mask))

# Run BFGS relaxation
opt = BFGS(slab)
opt.run(fmax=0.01)

# Calculate and print results
final_energy = slab.get_potential_energy()
final_z = slab.get_positions()[:, 2]
sorted_z = np.sort(final_z)
layer_avg_z = [np.mean(chunk) for chunk in np.array_split(sorted_z, 4)]

print(f"\nFinal relaxed total energy: {final_energy:.4f} eV")
for layer_num, avg_z in enumerate(layer_avg_z, 1):
    print(f"Layer {layer_num} (bottom to top) average z-coordinate: {avg_z:.4f} Å")
