from ase.build import bulk, surface
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# EOS to find equilibrium lattice constant
cu = bulk('Cu', 'fcc', a=3.6)
cell = cu.get_cell()
volumes, energies = [], []
for scale in np.linspace(0.95, 1.05, 11):
    atoms = cu.copy()
    atoms.set_cell(cell * scale, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = (v0 * 4) ** (1/3)  # FCC: 4 atoms per conventional cell, V_conv = a^3
print(f"Equilibrium lattice constant: {a0:.4f} Angstrom")

# Build (111) slab with 4 layers
cu_bulk = bulk('Cu', 'fcc', a=a0)
slab = surface(cu_bulk, (1, 1, 1), layers=4, vacuum=10.0)
slab.center(vacuum=10.0, axis=2)

# Identify bottom 2 layers by z coordinate
z_coords = slab.get_positions()[:, 2]
z_sorted = np.sort(np.unique(np.round(z_coords, 2)))
z_bottom2 = z_sorted[:2]

fixed_indices = [i for i, z in enumerate(z_coords) if round(z, 2) in np.round(z_bottom2, 2)]
constraint = FixAtoms(indices=fixed_indices)
slab.set_constraint(constraint)

# Attach EMT calculator
slab.calc = EMT()

# BFGS relaxation
opt = BFGS(slab, logfile=None)
opt.run(fmax=0.01)

# Results
final_energy = slab.get_potential_energy()
print(f"Final energy after relaxation: {final_energy:.4f} eV")

# Layer z-coordinate averages
positions = slab.get_positions()
z_vals = positions[:, 2]
z_rounded = np.round(z_vals, 1)
unique_z = np.sort(np.unique(z_rounded))

print("\nLayer z-coordinate averages (bottom to top):")
for i, uz in enumerate(unique_z):
    mask = np.abs(z_vals - uz) < 0.5
    mean_z = np.mean(z_vals[mask])
    print(f"  Layer {i+1}: z_mean = {mean_z:.4f} Angstrom")
