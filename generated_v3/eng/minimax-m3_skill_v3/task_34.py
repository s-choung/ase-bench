import numpy as np
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.mep import NEB
from scipy.spatial import Delaunay

# Cu(111) slab: 3x3 surface, 4 layers, 10 Å vacuum
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0, a=3.6)

# Identify layer z-coordinates
pos = slab.get_positions()
z = pos[:, 2]
unique_z = np.sort(np.unique(np.round(z, 2)))
top_z, sec_z = unique_z[-1], unique_z[-2]

# XY positions of top and 2nd layer
top_xy = pos[np.abs(z - top_z) < 0.1][:, :2]
sec_xy = pos[np.abs(z - sec_z) < 0.1][:, :2]

# Locate one fcc and one hcp hollow site via triangulation
# hcp = centroid with 2nd-layer atom directly below; fcc = no atom below
fcc_xyz = hcp_xyz = None
for simplex in Delaunay(top_xy).simplices:
    c = top_xy[simplex].mean(axis=0)
    is_hcp = np.any(np.linalg.norm(sec_xy - c, axis=1) < 0.5)
    s = np.array([c[0], c[1], top_z + 1.8])
    if is_hcp and hcp_xyz is None:
        hcp_xyz = s
    elif not is_hcp and fcc_xyz is None:
        fcc_xyz = s
    if fcc_xyz is not None and hcp_xyz is not None:
        break

# Initial (fcc) and final (hcp) configurations with adatom
initial = slab.copy(); initial.append('Cu'); initial.positions[-1] = fcc_xyz
final   = slab.copy(); final.append('Cu');   final.positions[-1]   = hcp_xyz

# Fix bottom 2 layers; do not fix the adatom
z_all = initial.positions[:, 2]
fix_mask = [zi < unique_z[1] + 0.1 for zi in z_all]
fix_mask[-1] = False

# NEB: initial + 5 intermediate images + final
images = [initial] + [initial.copy() for _ in range(5)] + [final]
neb = NEB(images)
neb.interpolate(method='idpp')

for img in images:
    img.set_constraint(FixAtoms(mask=fix_mask))
    img.calc = EMT()

BFGS(neb, trajectory='neb.traj').run(fmax=0.05)

# Energy barrier
energies = np.array([img.get_potential_energy() for img in images])
print(f"Initial energy:    {energies[0]:.4f} eV")
print(f"Maximum energy:    {energies.max():.4f} eV")
print(f"Diffusion barrier: {energies.max() - energies[0]:.4f} eV")
