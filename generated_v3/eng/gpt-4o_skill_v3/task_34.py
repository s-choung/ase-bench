from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB
from ase.io import Trajectory

# Initial and final states
slab = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)
add_adsorbate(slab, 'Cu', 1.8, 'fcc')
slab.set_calculator(EMT())
BFGS(slab).run(fmax=0.05)
initial = slab.copy()

slab = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)
add_adsorbate(slab, 'Cu', 1.8, 'hcp')
slab.set_calculator(EMT())
BFGS(slab).run(fmax=0.05)
final = slab.copy()

# Create NEB images
images = [initial] + [initial.copy() for _ in range(5)] + [final]
neb = NEB(images)
neb.interpolate(method='idpp')

# Set calculator for intermediate images
for image in images[1:-1]:
    image.set_calculator(EMT())

# Run NEB
opt = BFGS(neb)
opt.run(fmax=0.05)

# Calculate energy barrier
energies = [img.get_potential_energy() for img in images]
energy_barrier = max(energies) - energies[0]
print("Energy barrier:", energy_barrier, "eV")
