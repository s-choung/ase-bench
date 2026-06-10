import numpy as np
from ase.build import fcc111, add_adsorbate
from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB
from ase.constraints import FixAtoms

# Build Cu(111) slab
slab = fcc111('Cu', size=(4, 4, 4), vacuum=10.0)

# Fix bottom two layers
z_coords = slab.positions[:, 2]
z_min = z_coords.min()
bottom_indices = [i for i, z in enumerate(z_coords) if z < z_min + 2.5]
constraint = FixAtoms(indices=bottom_indices)

# Initial state: Cu adatom at fcc hollow
initial = slab.copy()
add_adsorbate(initial, Atoms('Cu'), height=1.5, position='fcc')
initial.set_constraint(constraint)
initial.calc = EMT()
BFGS(initial).run(fmax=0.05)

# Final state: Cu adatom at hcp hollow
final = slab.copy()
add_adsorbate(final, Atoms('Cu'), height=1.5, position='hcp')
final.set_constraint(constraint)
final.calc = EMT()
BFGS(final).run(fmax=0.05)

# NEB with 5 intermediate images
images = [initial] + [initial.copy() for _ in range(5)] + [final]
for img in images:
    img.set_constraint(constraint)
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='idpp')
BFGS(neb, trajectory='cu_diffusion_neb.traj').run(fmax=0.05)

# Print energy barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f'Energy barrier (fcc -> hcp): {barrier:.4f} eV')
