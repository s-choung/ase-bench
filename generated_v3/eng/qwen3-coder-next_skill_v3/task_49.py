import numpy as np
from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import EquationOfState
from ase.constraints import FixAtoms
from ase.units import Bohr

# Step 1: Find equilibrium lattice constant of Cu FCC using EOS
a0 = 3.61  # Initial guess for Cu lattice constant
atoms = bulk('Cu', 'fcc', a=a0)
atoms.calc = EMT()

volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(a0 * x * np.eye(3), scale_atoms=True)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = (v0 * 4 / np.pi) ** (1/3)  # FCC: V = 2*a^3/√2 = a^3/√2, but ASE bulk volume is a^3/4 for fcc
# Actually, ASE bulk volume is a^3 for cubic, so a = (v0*4)**(1/3) for fcc (4 atoms per unit cell)
a_eq = (v0 * 4) ** (1/3)

# Step 2: Create (111) 4-layer slab with equilibrium lattice constant
slab = fcc111('Cu', size=(3, 3, 4), a=a_eq, vacuum=15.0)

# Step 3: Fix bottom 2 layers
tags = slab.get_tags()
slab.set_constraint(FixAtoms(mask=[tag < 2 for tag in tags]))

# Step 4: Attach EMT calculator
slab.calc = EMT()

# Step 5: Run BFGS optimization
opt = BFGS(slab, trajectory='slab_opt.traj')
opt.run(fmax=0.01)

# Step 6: Print final energy and average z-coordinate for each layer
energy = slab.get_potential_energy()
print(f"Final energy: {energy:.6f} eV")

# Calculate average z per layer
z_coords = slab.get_positions()[:, 2]
z_avgs = []
for layer in range(4):
    layer_indices = np.where(tags == layer)[0]
    z_avgs.append(np.mean(z_coords[layer_indices]))

print("Layer z-averages (Å):")
for i, z_avg in enumerate(z_avgs):
    print(f"Layer {i}: {z_avg:.4f}")
