from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Create Cu(111) slab
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
slab.calc = EMT()

# Optimize clean slab
BFGS(slab).run(fmax=0.05)

# Create initial state (fcc hollow)
initial = slab.copy()
add_adsorbate(initial, 'Cu', height=1.5, position='fcc')
initial.calc = EMT()
BFGS(initial).run(fmax=0.05)

# Create final state (hcp hollow)
final = slab.copy()
add_adsorbate(final, 'Cu', height=1.5, position='hcp')
final.calc = EMT()
BFGS(final).run(fmax=0.05)

# Create NEB images
images = [initial] + [initial.copy() for _ in range(5)] + [final]
neb = NEB(images)
neb.interpolate(method='idpp')

# Set calculators for intermediate images
for image in images[1:-1]:
    image.calc = EMT()

# Run NEB optimization
BFGS(neb).run(fmax=0.05)

# Calculate energy barrier
energies = [image.get_potential_energy() for image in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.3f} eV")
