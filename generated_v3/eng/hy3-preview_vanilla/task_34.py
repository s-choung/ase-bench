from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.neb import NEB
from ase import Atoms
import numpy as np

# Build Cu FCC(111) slab
slab = fcc111('Cu', size=(2, 2, 3), vacuum=10.0)
mask = [atom.tag > 2 for atom in slab]  # Fix bottom layer
slab.set_constraint(FixAtoms(mask=mask))

# Initial state: adatom at fcc hollow site
initial = slab.copy()
add_adsorbate(initial, 'Cu', height=2.0, position='fcc')

# Final state: adatom at hcp hollow site
final = slab.copy()
add_adsorbate(final, 'Cu', height=2.0, position='hcp')

# Setup NEB
initial.calc = final.calc = ASE.EMT()
images = [initial]
for i in range(3):
    image = initial.copy()
    image.calc = ASE.EMT()
    images.append(image)
images.append(final)

neb = NEB(images, climb=True, method='improvedtangent')
neb.interpolate('idpp')

# Run NEB
optimizer = BFGS(neb, trajectory='neb.traj')
optimizer.run(fmax=0.05)

# Calculate barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.3f} eV")
