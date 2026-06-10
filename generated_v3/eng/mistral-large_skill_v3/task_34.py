from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB
from ase.io import write
import numpy as np

# Build slab and adatom
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
add_adsorbate(slab, 'Cu', height=1.8, position='fcc')
slab.calc = EMT()
BFGS(slab).run(fmax=0.01)

# Create final state (hcp site)
final = slab.copy()
final.positions[-1] = slab.positions[-1] + slab.cell[0, :2] / 3 - slab.cell[1, :2] / 3

# NEB setup
images = [slab] + [slab.copy() for _ in range(5)] + [final]
neb = NEB(images)
neb.interpolate(method='idpp')

# Relax images
for img in images[1:-1]:
    img.calc = EMT()
BFGS(neb).run(fmax=0.05)

# Calculate barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.3f} eV")
