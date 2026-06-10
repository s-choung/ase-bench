from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.neb import NEB, idpp_interpolate
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
import numpy as np

# Build Cu(111) slab
slab = fcc111('Cu', size=(2, 2, 3), vacuum=10.0)
add_adsorbate(slab, 'Cu', height=1.8, position='fcc')

# Define initial (fcc) and final (hcp) positions manually
fcc_pos = slab[-1].position.copy()
hcp_pos = slab.get_positions()[-1].copy()
hcp_pos[0] += slab.cell[0, 0] / 2  # shift in x
hcp_pos[1] += slab.cell[1, 1] / 6  # shift in y to hcp site

slab[-1].position = fcc_pos  # ensure initial is fcc
images = [slab.copy() for _ in range(5)]
images[-1][-1].position = hcp_pos  # set final adatom position to hcp

# Set EMT calculator and fix lower layer
for img in images:
    img.calc = EMT()
    mask = [atom.tag > 1 for atom in img]
    img.set_constraint(FixAtoms(mask=mask))

# NEB with IDPP
neb = NEB(images)
neb.interpolate(method='idpp')
neb.climb = True
neb.parallel = False

# Optimize NEB
from ase.optimize import BFGS
qn = BFGS(neb, logfile='neb.log')
qn.run(fmax=0.05)

# Get energies and compute barrier
energies = [img.get_potential_energy() for img in images]
energy_barrier = max(energies) - energies[0]
print(f"Energy barrier: {energy_barrier:.3f} eV")
