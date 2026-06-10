from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Create Cu(111) slab
slab = fcc111('Cu', size=(4, 4, 4), vacuum=10.0)

# Initial state: adatom at fcc hollow
initial = slab.copy()
add_adsorbate(initial, 'Cu', height=1.8, position='fcc')

# Final state: adatom at hcp hollow
final = slab.copy()
add_adsorbate(final, 'Cu', height=1.8, position='hcp')

# Set calculator and constrain slab atoms (fix all but adatom)
for atoms in (initial, final):
    atoms.calc = EMT()
    constraint = FixAtoms(indices=list(range(len(atoms) - 1)))
    atoms.set_constraint(constraint)

# Build NEB with 5 images (3 intermediate)
images = [initial] + [initial.copy() for _ in range(3)] + [final]

# Ensure all images have calculator
for img in images:
    img.calc = EMT()

# IDPP interpolation
neb = NEB(images)
neb.interpolate('idpp')

# Optimize path
optimizer = BFGS(neb, trajectory='neb.traj')
optimizer.run(fmax=0.05)

# Calculate and print barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f'Diffusion barrier: {barrier:.3f} eV')
