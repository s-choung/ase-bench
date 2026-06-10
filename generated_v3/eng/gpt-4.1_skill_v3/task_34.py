import numpy as np
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS
from ase import units

# Build Cu(111) slab
slab = fcc111('Cu', size=(3,3,4), vacuum=10.0)
mask = [atom.tag >= 3 for atom in slab]  # Fix bottom two layers
slab.set_constraint(FixAtoms(mask=mask))

# Get fcc and hcp hollow positions (center of triangle formed by three Cu atoms)
def get_hollow_pos(slab, kind='fcc'):
    pos = slab.get_positions()
    zmax = pos[:,2].max()
    # Consider only surface atoms (top layer)
    surface = [atom for atom in slab if abs(atom.position[2] - zmax) < 1e-2]
    # Corner atoms: (fcc and hcp positions relative to lattice vectors)
    # Unit cell: a1 = [a,0,0], a2 = [a/2, a*sqrt(3)/2, 0]
    cell = slab.get_cell()
    a1, a2 = cell[0], cell[1]
    o = np.zeros(3)
    # Fractional positions in x-y for fcc (1/3,1/3), hcp (2/3,2/3)
    fcc_frac = (1/3, 1/3)
    hcp_frac = (2/3, 2/3)
    xy = fcc_frac if kind=='fcc' else hcp_frac
    posxy = xy[0]*a1[:2] + xy[1]*a2[:2]
    # Place adatom above the average top layer height + 1.8 Å
    height = zmax + 1.8
    return np.array([posxy[0], posxy[1], height])

# Initial state: adatom at fcc hollow
initial = slab.copy()
add_adsorbate(initial, 'Cu', height=1.8, position=get_hollow_pos(slab, 'fcc')[:2])

# Final state: adatom at hcp hollow
final = slab.copy()
add_adsorbate(final, 'Cu', height=1.8, position=get_hollow_pos(slab, 'hcp')[:2])

# NEB images
images = [initial]
for i in range(5):
    images.append(initial.copy())
images.append(final)
neb = NEB(images)
neb.interpolate(method='idpp')

# Set calculator for each image
for img in images:
    img.calc = EMT()

# Optimize NEB path
opt = BFGS(neb)
opt.run(fmax=0.05)

# Energies
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f'Energy barrier (eV): {barrier:.3f}')
