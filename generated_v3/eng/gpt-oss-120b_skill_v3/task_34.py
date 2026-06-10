from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.mep import NEB
import numpy as np

# Build Cu(111) slab
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0, a=3.6)

# Initial (fcc hollow) and final (hcp hollow) states
initial = slab.copy()
add_adsorbate(initial, 'Cu', height=1.8, position='fcc')
final = slab.copy()
add_adsorbate(final, 'Cu', height=1.8, position='hcp')

# Fix substrate atoms (all but the adatom)
fix_idx = list(range(len(slab)))        # indices of slab atoms
constraint = FixAtoms(indices=fix_idx)
initial.set_constraint(constraint)
final.set_constraint(constraint)

# Attach calculator
calc = EMT()
initial.calc = calc
final.calc = calc

# Create intermediate images
n_inter = 5
images = [initial] + [initial.copy() for _ in range(n_inter)] + [final]

# Same constraints & calculator for intermediates
for img in images[1:-1]:
    img.set_constraint(constraint)
    img.calc = calc

# NEB with IDPP interpolation
neb = NEB(images)
neb.interpolate(method='idpp')

# Optimize the path
opt = BFGS(neb, trajectory='neb.traj')
opt.run(fmax=0.05)

# Energy barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f'Energy barrier: {barrier:.3f} eV')
