from ase import units
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Create Cu(111) slab
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()

# Optimize initial structure
BFGS(slab).run(fmax=0.05)

# Initial state: fcc hollow site
initial = slab.copy()
add_adsorbate(initial, 'Cu', 1.8, position='fcc')

# Final state: hcp hollow site
final = slab.copy()
add_adsorbate(final, 'Cu', 1.8, position='hcp')

# Set up NEB
images = [initial] + [initial.copy() for _ in range(5)] + [final]
neb = NEB(images)
neb.interpolate(method='idpp')

# Attach calculator to all intermediate images
for img in images[1:-1]:
    img.calc = EMT()

# Optimize NEB path
opt = BFGS(neb, trajectory=None)
opt.run(fmax=0.05)

# Get energies
energies = [img.get_potential_energy() for img in images]
energy_barrier = max(energies) - energies[0]
print(f"Energy barrier: {energy_barrier:.3f} eV")
