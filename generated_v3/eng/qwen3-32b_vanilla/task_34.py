from ase.build import fcc111, Atoms
from ase.neb import NEB
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase import neb as neb_utils

# Create Cu(111) slab
slab = fcc111('Cu', (1, 1, 1), layers=3, a=3.6, vacuum=10.0)

# Identify top-layer atoms
positions = slab.get_positions()
z_coords = positions[:, 2]
top_indices = [i for i, z in enumerate(z_coords) if z == max(z_coords)]

# fcc and hcp hollow site positions (x, y, z)
fcc = positions[top_indices[:3]].mean(axis=0)
fcc[2] += 2.0
hcp = positions[top_indices[1:4]].mean(axis=0)
hcp[2] += 2.0

# Create initial/final configurations
initial = slab.copy()
initial += Atoms('Cu', positions=[fcc])
final = slab.copy()
final += Atoms('Cu', positions=[hcp])

# Setup NEB images
images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb_utils.interpolate(images, method='idpp')

# Attach EMT calculator
for img in images:
    img.set_calculator(EMT())

# Optimize path
neb = NEB(images)
BFGS(neb).run(fmax=0.05)

# Calculate energy barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f'Energy barrier: {barrier:.4f} eV')
