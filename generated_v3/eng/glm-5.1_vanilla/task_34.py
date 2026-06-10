from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep.neb import NEB
from ase.vibrations import Vibrations

# Build Cu(111) surface
slab = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)
slab.pbc = True

# Initial state: adatom at fcc hollow
initial = slab.copy()
add_adsorbate(initial, 'Cu', height=1.8, position='fcc')

# Final state: adatom at hcp hollow
final = slab.copy()
add_adsorbate(final, 'Cu', height=1.8, position='hcp')

# Relax endpoints
for atoms in [initial, final]:
    atoms.calc = EMT()
    dyn = BFGS(atoms, logfile=None)
    dyn.run(fmax=0.05)

# Create 5 images and interpolate with IDPP
images = [initial]
images += [initial.copy() for _ in range(5)]
images += [final]

neb = NEB(images, climb=True)
neb.interpolate(method='idpp')

# Attach EMT calculator to images
for image in images[1:6]:
    image.calc = EMT()

# Run NEB
dyn_neb = BFGS(neb, logfile=None)
dyn_neb.run(fmax=0.05)

# Calculate and print energy barrier
energies = [image.get_potential_energy() for image in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.4f} eV")
