from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS
from ase.calculators.emt import EMT
import numpy as np

# Build Cu FCC(111) slab and fix bottom layers
slab = fcc111('Cu', size=(2,2,4), vacuum=10.0)
slab.set_constraint(FixAtoms(mask=[a.tag >= 1 for a in slab]))

# Initial (fcc hollow) and final (hcp hollow) adatom states
initial = slab.copy()
final = slab.copy()
add_adsorbate(initial, 'Cu', height=1.8, position='fcc')
add_adsorbate(final, 'Cu', height=1.8, position='hcp')

# NEB setup with 5 intermediate images and IDPP interpolation
images = [initial] + [initial.copy() for _ in range(5)] + [final]
for img in images:
    img.calc = EMT()
neb = NEB(images)
neb.interpolate(method='idpp')

# Optimize diffusion path
opt = BFGS(neb)
opt.run(fmax=0.05)

# Calculate and print energy barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f'Energy barrier: {barrier:.3f} eV')
