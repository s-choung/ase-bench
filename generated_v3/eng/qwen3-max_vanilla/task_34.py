from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.neb import NEB, interpolate
from ase.optimize import BFGS

# Create Cu(111) surface slab
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
slab.calc = EMT()

# Add Cu adatom at fcc hollow (initial state)
initial = slab.copy()
add_adsorbate(initial, 'Cu', height=1.8, position='fcc')

# Add Cu adatom at hcp hollow (final state)
final = slab.copy()
add_adsorbate(final, 'Cu', height=1.8, position='hcp')

# Set calculator for end points
initial.calc = EMT()
final.calc = EMT()

# Relax end points
opt_init = BFGS(initial)
opt_init.run(fmax=0.05)
opt_final = BFGS(final)
opt_final.run(fmax=0.05)

# Create NEB images
images = [initial]
for i in range(5):
    images.append(initial.copy())
images.append(final)

# IDPP interpolation
neb = NEB(images)
interpolate(images, method='idpp')

# Attach calculator to all images
for image in images[1:-1]:
    image.calc = EMT()

# Optimize NEB path
opt = BFGS(neb, trajectory='diffusion.traj')
opt.run(fmax=0.05)

# Extract energies
energies = [image.get_potential_energy() for image in images]
barrier = max(energies) - energies[0]
print(f'Energy barrier: {barrier:.3f} eV')
