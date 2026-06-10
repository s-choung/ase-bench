from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import MDMin
from ase.calculators.emt import EMT
import numpy as np

# Set up the Cu(111) surface
slab = fcc111('Cu', size=(3, 3, 2), vacuum=10.0)
add_adsorbate(slab, 'Cu', 1, 'hollow', 'fcc')

# Fix the bottom layer
slab.set_constraint(FixAtoms(mask=np.array([atom.tag < 2 for atom in slab])))
slab.set_calculator(EMT())

# Define initial and final states
initial = slab.copy()
initial[0].position[-1] -= 0.1  # Adjust to fcc hollow

final = slab.copy()
final[0].position[-1] += 0.1  # Adjust to hcp hollow

# Set up NEB calculation
images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = NEB(images, interpolate='idpp', climb=True)

# Optimize NEB path
optimizer = MDMin(neb, traj='neb.traj', logfile='neb.log')
optimizer.run(fmax=0.05)

# Extract energies and calculate barrier
energies = np.array([image.get_potential_energy() for image in images])
barrier = max(energies) - min(energies)

print(f'Energy barrier: {barrier:.4f} eV')
