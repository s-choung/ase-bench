import numpy as np
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Build Cu(111) slab
size = (2, 2, 4)
slab = fcc111('Cu', size=size, vacuum=10.0)
slab.set_constraint(FixAtoms(mask=[a.z < slab.cell[2, 2] / 2 for a in slab]))

# Calculate primitive lattice vectors for site positioning
a1_prim = slab.cell[0] / size[0]
a2_prim = slab.cell[1] / size[1]

# Define FCC and HCP hollow positions
fcc_pos = (2/3) * a1_prim + (1/3) * a2_prim
hcp_pos = (1/3) * a1_prim + (2/3) * a2_prim

# Create initial (FCC) and final (HCP) states
initial = slab.copy()
add_adsorbate(initial, 'Cu', 1.85, position=fcc_pos[:2])

final = slab.copy()
add_adsorbate(final, 'Cu', 1.85, position=hcp_pos[:2])

# Relax endpoints
calc = EMT()
initial.calc = calc
final.calc = calc
BFGS(initial).run(fmax=0.05)
BFGS(final).run(fmax=0.05)

# Setup NEB with 5 images and IDPP interpolation
images = [initial] + [initial.copy() for _ in range(5)] + [final]
neb = NEB(images, interpolation='idpp')

# Attach calculators and optimize band
for image in images:
    image.calc = EMT()
BFGS(neb).run(fmax=0.05)

# Calculate and print barrier
energies = [image.get_potential_energy() for image in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.3f} eV")
