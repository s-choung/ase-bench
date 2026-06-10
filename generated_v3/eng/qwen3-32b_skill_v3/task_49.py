from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import EquationOfState
from ase.constraints import FixAtoms
import numpy as np

# Generate EOS data for Cu FCC
a_values = np.linspace(3.5, 3.8, 7)
volumes, energies = [], []
for a in a_values:
    cu_bulk = bulk('Cu', 'fcc', a=a, cubic=True)
    cu_bulk.calc = EMT()
    volumes.append(cu_bulk.get_volume())
    energies.append(cu_bulk.get_potential_energy())

# Fit EOS and get equilibrium lattice constant
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = v0 ** (1/3)

# Create (111) slab with equilibrium lattice constant
slab = fcc111('Cu', size=(2, 2, 4), a=a0, vacuum=10.0)
slab.calc = EMT()

# Fix bottom 2 layers
n_atoms_per_layer = 4  # (2×2)
fixed_indices = list(range(n_atoms_per_layer * 2))
slab.set_constraint(FixAtoms(indices=fixed_indices))

# Relax slab
opt = BFGS(slab)
opt.run(fmax=0.05)

# Output results
print(f"Final energy: {slab.get_potential_energy():.4f} eV")
positions = slab.get_positions()
layers = 4
n_atoms_total = len(slab)
per_layer = n_atoms_total // layers
z_coords = positions[:, 2]

averages = [np.mean(z_coords[i*per_layer:(i+1)*per_layer]) for i in range(layers)]
print("Average z-coordinates per layer (Å):", [f"{z:.3f}" for z in averages])
