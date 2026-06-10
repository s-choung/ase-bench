from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.neb import NEB, idpp_interpolate
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create FCC(111) slab
slab = fcc111('Cu', size=(2, 2, 3), vacuum=6.0)
slab.calc = EMT()

# Add adatom at fcc hollow site
add_adsorbate(slab, 'Cu', height=1.5, position='fcc')
slab.set_constraint([fix for fix in slab.constraints] if slab.constraints else [])
initial = slab.copy()

# Optimize initial state
optimizer_i = BFGS(initial)
optimizer_i.run(fmax=0.05)

# Move adatom to hcp hollow site
add_adsorbate(slab, 'Cu', height=1.5, position='hcp')
final = slab.copy()

# Optimize final state
optimizer_f = BFGS(final)
optimizer_f.run(fmax=0.05)

# Create NEB images
images = [initial]
images += [initial.copy() for _ in range(3)]
images.append(final)
neb = NEB(images, climb=True)
neb.interpolate()
idpp_interpolate(neb, fmax=0.1)

# Set calculator and optimize
for image in images:
    image.calc = EMT()
optimizer = BFGS(neb, trajectory='neb.traj')
optimizer.run(fmax=0.05)

# Calculate energy barrier
energies = [image.get_potential_energy() for image in images]
barrier = max(energies) - energies[0]
print(f'Energy barrier: {barrier:.4f} eV')
