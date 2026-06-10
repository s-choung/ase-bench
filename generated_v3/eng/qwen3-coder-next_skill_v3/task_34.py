from ase import Atoms, units
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB
from ase.mep.autoneb import AutoNEB
from ase.io import write
import numpy as np

# Create Cu(111) slab with 4 layers and vacuum
slab = fcc111('Cu', size=(3, 3, 4), vacuum=12.0)
slab.set_pbc((True, True, False))

# Set calculator
slab.calc = EMT()

# Add Cu adatom at hollow site (bridge site initially, near center)
# For FCC(111), hollow sites are 3-fold (fcc and hcp)
# Let's place it above the hollow site (fcc) at z ~ 1.7 Å
slab.append('Cu')
slab.positions[-1] = np.array([np.mean(slab.positions[:len(slab)-1], axis=0)[:2] + [1.5, 0.87], 1.7])

# Fix bottom 2 layers
mask = [a.tag < 3 for a in slab]
slab.set_constraint(ase.constraints.FixAtoms(mask=mask))

# Optimize initial state
BFGS(slab).run(fmax=0.05)
initial = slab.copy()

# Move adatom to hcp hollow site (shift by 1/3,1/3 in fractional coords)
slab2 = slab.copy()
# Get fractional coordinates, shift, convert back
cell = slab2.get_cell()
frac_pos = cell.scaled_positions(slab2.positions)
frac_pos[-1, 0] += 1/3
frac_pos[-1, 1] += 1/3
frac_pos[-1, :2] %= 1  # Wrap back to cell
slab2.positions = cell.cartesian_positions(frac_pos)
# Keep same height
slab2.positions[-1, 2] = 1.7

# Optimize final state
BFGS(slab2).run(fmax=0.05)
final = slab2.copy()

# Create 5 images (total 7 including endpoints)
images = [initial] + [initial.copy() for _ in range(5)] + [final]

# IDPP interpolation
neb = NEB(images)
neb.interpolate(method='idpp')

# Set calculator for all images
for img in images:
    img.calc = EMT()

# Run NEB optimization with AutoNEB
autoneb = AutoNEB(neb, fmax=0.05, min_images=5, optimizer='BFGS')
autoneb.run()

# Find maximum energy and calculate barrier
energies = [img.get_potential_energy() for img in images]
E_initial = energies[0]
E_max = max(energies)
barrier = E_max - E_initial

print(f"Energy barrier: {barrier:.3f} eV")
