from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import BFGS
import numpy as np

# Build Cu(111) slab (3x3, 3 layers, vacuum 10 Å)
a = 3.61  # Cu lattice constant (EMT default)
slab = fcc111('Cu', size=(3, 3, 3), a=a, vacuum=10.0)

# Create initial and final configurations with adatom at fcc and hcp hollow
initial = slab.copy()
add_adsorbate(initial, 'Cu', position='fcc', height=1.5)
final = slab.copy()
add_adsorbate(final, 'Cu', position='hcp', height=1.5)

# Set calculator
calc = EMT()
initial.set_calculator(calc)
final.set_calculator(calc)

# Relax endpoints: fix bottom two layers (indices where z < cutoff)
z_vals = initial.positions[:, 2]
cutoff = z_vals.min() + 1.5  # approximate bottom two layers
fix_indices = np.where(z_vals < cutoff)[0]
constraint = FixAtoms(indices=fix_indices)
initial.set_constraint(constraint)
final.set_constraint(constraint)

opt1 = BFGS(initial)
opt1.run(fmax=0.01)
opt2 = BFGS(final)
opt2.run(fmax=0.01)

# After relaxation, remove constraints to avoid issues in NEB? We'll reapply.
initial.set_constraint()
final.set_constraint()

# Build NEB images: 5 interior images
n_images = 5
images = [initial]
for _ in range(n_images):
    images.append(initial.copy())
images.append(final)

# Set same constraints for all images: fix all slab atoms, allow adatom to move
slab_indices = list(range(len(slab)))
for image in images:
    image.set_constraint(FixAtoms(indices=slab_indices))
    image.set_calculator(calc)

# Interpolate using IDPP
neb = NEB(images)
neb.interpolate(method='idpp')

# Optimize the band
opt = BFGS(neb, trajectory='neb.traj')
opt.run(fmax=0.01)

# Compute and print energy barrier
energies = [image.get_potential_energy() for image in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.3f} eV")
