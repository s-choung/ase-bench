from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.mep import NEB
import numpy as np

# Build slab
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
slab.set_constraint(FixAtoms(indices=[a.index for a in slab if a.tag >= 3]))
slab.calc = EMT()
BFGS(slab, logfile=None).run(fmax=0.05)

# Get surface layer info for adsorption site positions
from ase.build import fcc111
a_Cu = 3.6  # Cu lattice constant

# Build initial (fcc hollow) and final (hcp hollow) structures
def make_slab_with_adatom(site):
    s = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
    s.set_constraint(FixAtoms(indices=[a.index for a in s if a.tag >= 3]))
    from ase import Atom
    add_adsorbate(s, 'Cu', height=2.1, position=site)
    return s

# fcc hollow and hcp hollow positions on (3x3) fcc111
# On fcc111, fcc hollow is above 3rd layer atom, hcp hollow is above 2nd layer atom
# Use fractional coordinates of the surface unit cell
cell = slab.get_cell()

# Surface unit vectors
a1 = cell[0][:2]
a2 = cell[1][:2]

# For 3x3 supercell, place adatom at fcc and hcp hollow sites
# fcc hollow: (1/3, 1/3) in fractional coords of supercell -> (1/9, 1/9) of 3x3
# Use explicit positions
# fcc hollow site (fractional of supercell)
fcc_frac = np.array([1/3, 1/6])
hcp_frac = np.array([1/3, 1/2])

fcc_pos = fcc_frac[0]*a1 + fcc_frac[1]*a2
hcp_pos = hcp_frac[0]*a1 + hcp_frac[1]*a2

# Build initial and final slabs
initial = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
initial.set_constraint(FixAtoms(indices=[a.index for a in initial if a.tag >= 3]))
add_adsorbate(initial, 'Cu', height=2.1, position=tuple(fcc_pos))

final = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
final.set_constraint(FixAtoms(indices=[a.index for a in final if a.tag >= 3]))
add_adsorbate(final, 'Cu', height=2.1, position=tuple(hcp_pos))

# Relax initial and final
initial.calc = EMT()
BFGS(initial, logfile=None).run(fmax=0.05)

final.calc = EMT()
BFGS(final, logfile=None).run(fmax=0.05)

# NEB setup with 5 images
n_images = 5
images = [initial.copy()] + [initial.copy() for _ in range(n_images)] + [final.copy()]

neb = NEB(images)
neb.interpolate(method='idpp')

for img in images[1:-1]:
    img.calc = EMT()

# Run NEB
opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05, steps=500)

# Collect energies
energies = [img.get_potential_energy() for img in images]
e_initial = energies[0]
e_barrier = max(energies) - e_initial

print(f"Image energies (eV): {[f'{e:.4f}' for e in energies]}")
print(f"Initial energy: {e_initial:.4f} eV")
print(f"Maximum energy: {max(energies):.4f} eV")
print(f"Energy barrier: {e_barrier:.4f} eV")
