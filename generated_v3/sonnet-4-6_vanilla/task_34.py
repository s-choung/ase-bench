```python
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.neb import NEB
from ase.neb import interpolate
import numpy as np

# Build Cu(111) slab
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
slab.calc = EMT()

# Relax slab
opt = BFGS(slab, logfile=None)
opt.run(fmax=0.05)

# Get lattice constant and surface info
a = 3.6  # Cu lattice constant approx
pos = slab.get_positions()
z_top = pos[:, 2].max()

# Find fcc hollow site
# In fcc111, fcc hollow is above 3rd layer atom, hcp hollow is above 2nd layer atom
# Use ASE's surface sites approach manually
# Cell vectors
cell = slab.get_cell()
cx = cell[0, 0]
cy = cell[1, 1]

# Top layer atoms
top_layer_z = sorted(set(np.round(pos[:, 2], 2)))[-1]
top_atoms = [i for i, p in enumerate(pos) if abs(p[2] - top_layer_z) < 0.1]

# Second layer atoms
second_layer_z = sorted(set(np.round(pos[:, 2], 2)))[-2]
second_atoms = [i for i, p in enumerate(pos) if abs(p[2] - second_layer_z) < 0.1]

# Third layer atoms
third_layer_z = sorted(set(np.round(pos[:, 2], 2)))[-3]
third_atoms = [i for i, p in enumerate(pos) if abs(p[2] - third_layer_z) < 0.1]

# fcc hollow: center of triangle of top layer atoms, no atom below in 2nd layer directly
# hcp hollow: center of triangle of top layer atoms, with 2nd layer atom below

top_pos = pos[top_atoms]
second_pos = pos[second_atoms]
third_pos = pos[third_atoms]

# Find triangles in top layer
# Sort top atoms by x, y
top_xy = top_pos[:, :2]

# Find nearest neighbors for first top atom
ref = top_xy[0]
dists = np.linalg.norm(top_xy - ref, axis=1)
nn_idx = np.argsort(dists)[1:3]  # 2 nearest neighbors

# Triangle center (fcc or hcp hollow candidate)
tri_center = (top_xy[0] + top_xy[nn_idx[0]] + top_xy[nn_idx[1]]) / 3.0
tri_z = z_top + 2.0  # adatom height above surface

# Check if there's a 2nd layer atom below tri_center -> hcp hollow
# or 3rd layer atom -> fcc hollow
def has_atom_below(center_xy, layer_pos, tol=0.5):
    for p in layer_pos:
        d = np.linalg.norm(p[:2] - center_xy)
        if d < tol:
            return True
    return False

# The two hollow sites near our triangle
# fcc hollow: no 2nd layer atom directly below
# hcp hollow: 2nd layer atom directly below

# Generate candidate hollow sites by shifting
# In fcc111 3x3, find all hollow sites
from itertools import combinations

def find_hollow_sites(top_pos, second_pos, third_pos, z_ads=2.0):
    fcc_hollows = []
    hcp_hollows = []
    n = len(top_pos)
    for i, j, k in combinations(range(n), 3):
        p1, p2, p3 = top_pos[i, :2], top_pos[j, :2], top_pos[k, :2]
        d12 = np.linalg.norm(p1 - p2)
        d13 = np.linalg.norm(p1 - p3)
        d23 = np.linalg.norm(p2 - p3)
        nn_dist = 2.556  # Cu nn distance on 111
        if abs(d12 - nn_dist) < 0.3 and abs(d13 - nn_dist) < 0.3 and abs(d23 - nn_dist) < 0.3:
            center = (p1 + p2 + p3) / 3.0
            if has_atom_below(center, second_pos, tol=0.5):
                hcp_hollows.append(np.array([center[0], center[1], top_pos[i, 2] + z_ads]))
            elif has_atom_below(center, third_pos, tol=0.5):
                fcc_hollows.append(np.array([center[0], center[1], top_pos[i, 2] + z_ads]))
    return fcc_hollows, hcp_hollows

fcc_hollows, hcp_hollows = find_hollow_sites(top_pos, second_pos, third_pos, z_ads=2.0)

print(f"Found {len(fcc_hollows)} fcc hollows, {len(hcp_hollows)} hcp hollows")

# Pick adjacent fcc and hcp hollow (minimum distance pair)
min_dist = 1e10
best_fcc = None
best_hcp = None
for fh in fcc_hollows:
    for hh in hcp_hollows:
        d = np.linalg.norm(fh[:2] - hh[:2])
        if d < min_dist:
            min_dist = d
            best_fcc = fh
            best_hcp = hh

print(f"fcc hollow: {best_fcc}")
print(f"hcp hollow: {best_hcp}")
print(f"Distance between hollows: {min_dist:.3f} Ang")

# Build initial and final structures
def make_slab_with_adatom(slab_relaxed, adatom_pos):
    from ase import Atoms
    atoms = slab_relaxed.copy()
    atoms.append('Cu')
    positions = atoms.get_positions()
    positions[-1] = adatom_pos
    atoms.set_positions(positions)
    return atoms

initial = make_slab_with_adatom(slab, best_fcc)
final = make_slab_with_adatom(slab, best_hcp)

# Relax initial and final
initial.calc = EMT()
opt_i = BFGS(initial, logfile=None)
opt_i.run(fmax=0.05)

final.calc = EMT()
opt_f = BFGS(final, logfile=None)
opt_f.run(fmax=0.05)

E_initial = initial.get_potential_energy()
E_final = final.get_potential_energy()
print(f"Initial energy: {E_initial:.4f} eV")
print(f"Final energy:   {E_final:.4f} eV")

# NEB with 5 images (including endpoints = 7 total, 5 intermediate)
n_images = 5
images = [initial.copy()]
for i in range(n_images):
    image = initial.copy()
    image.calc = EMT()
    images.append(image)
images.append(final.copy())
images[-1].calc = EMT()

# IDPP interpolation
neb = NEB(images)
neb.interpolate(method='idpp')

# Run NEB optimization
optimizer = BFGS(neb, logfile=None)
optimizer.run(fmax=0.05, steps=500)

# Collect energies
energies = [img.get_potential_energy() for img in images]
print("\nNEB image energies (eV):")
for i, e in enumerate(energies):
    print(f"  Image {i}: {e:.4f} eV")
