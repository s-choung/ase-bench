from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS
from ase.io import read, write
import numpy as np

# Create Cu(111) surface
slab = fcc111('Cu', size=(4, 4, 3), a=3.61, vacuum=10.0)
slab.set_calculator(EMT())

# Optimize slab
opt = BFGS(slab, trajectory='slab.traj')
opt.run(fmax=0.01)

# Create initial state: adatom at fcc hollow
initial = slab.copy()
add_adsorbate(initial, 'Cu', height=2.0, position='fcc')
initial.set_calculator(EMT())
opt_initial = BFGS(initial, trajectory='initial.traj')
opt_initial.run(fmax=0.01)

# Create final state: adatom at hcp hollow
final = slab.copy()
add_adsorbate(final, 'Cu', height=2.0, position='hcp')
final.set_calculator(EMT())
opt_final = BFGS(final, trajectory='final.traj')
opt_final.run(fmax=0.01)

# NEB calculation with 5 images
neb = NEB([initial, final], k=0.1, climb=False)
neb.interpolate(method='idpp')

# Set calculators for all images
for image in neb.images:
    image.set_calculator(EMT())

# Run NEB
opt_neb = BFGS(neb, trajectory='neb.traj')
opt_neb.run(fmax=0.05)

# Calculate energy barrier
energies = [image.get_potential_energy() for image in neb.images]
initial_energy = energies[0]
max_energy = max(energies)
barrier = max_energy - initial_energy

print(f"Initial energy: {initial_energy:.4f} eV")
print(f"Final energy: {energies[-1]:.4f} eV")
print(f"Maximum energy: {max_energy:.4f} eV")
print(f"Energy barrier: {barrier:.4f} eV")
print(f"All image energies: {[f'{e:.4f}' for e in energies]}")
