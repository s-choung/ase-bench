from ase.build import fcc111
from ase.calculators.emt import EMT
from ase import Atoms
import numpy as np

# Parameters
a = 3.92           # Pt lattice constant (Å)
d_OH = 0.98        # O-H bond length (Å)
d_PtO = 2.0        # desired Pt-O distance (Å)
vacuum = 10.0

# Build 3-layer Pt(111) slab with 2x2 surface cell
slab = fcc111('Pt', size=(2, 2, 3), a=a, vacuum=vacuum)
pos = slab.get_positions()
z_coords = pos[:, 2]
z_surf = np.max(z_coords)

# Identify surface (top) layer atoms
surf_mask = np.abs(z_coords - z_surf) < 0.1
surf_indices = np.where(surf_mask)[0]
surf_pos = pos[surf_indices]

# Nearest-neighbour distance on the surface
n_surf = len(surf_pos)
dist = np.zeros((n_surf, n_surf))
for i in range(n_surf):
    for j in range(n_surf):
        dxy = surf_pos[i, :2] - surf_pos[j, :2]
        dist[i, j] = np.sqrt(np.dot(dxy, dxy))
d_PtPt = np.min(dist[dist > 0])

# ----- Ontop site -----
ontop_pt = surf_pos[0]
ontop_z = z_surf + d_PtO

# ----- Bridge site -----
bridge_pair = None
for i in range(n_surf):
    for j in range(i+1, n_surf):
        if np.abs(dist[i, j] - d_PtPt) < 0.01:
            bridge_pair = (i, j)
            break
    if bridge_pair is not None:
        break
pt1, pt2 = surf_pos[bridge_pair[0]], surf_pos[bridge_pair[1]]
bridge_center = (pt1[:2] + pt2[:2]) / 2.0
bridge_dz = np.sqrt(max(0, d_PtO**2 - (d_PtPt/2)**2))
bridge_z = z_surf + bridge_dz

# ----- fcc hollow site -----
# Find all surface equilateral triangles
triangles = []
for i in range(n_surf):
    for j in range(i+1, n_surf):
        if np.abs(dist[i, j] - d_PtPt) < 0.01:
            for k in range(j+1, n_surf):
                if (np.abs(dist[i, k] - d_PtPt) < 0.01 and
                    np.abs(dist[j, k] - d_PtPt) < 0.01):
                    triangles.append((i, j, k))

# Middle (second) layer atoms
z_sorted = sorted(set(z_coords))
z_mid = z_sorted[-2]
mid_mask = np.abs(z_coords - z_mid) < 0.01
mid_xy = pos[mid_mask][:, :2]
d_111 = z_surf - z_mid

# Identify fcc hollow: no middle-layer atom directly under the centroid
fcc_centroid = None
for tri in triangles:
    i, j, k = tri
    centroid = (surf_pos[i][:2] + surf_pos[j][:2] + surf_pos[k][:2]) / 3.0
    if not any(np.linalg.norm(centroid - m) < 0.5 for m in mid_xy):
        fcc_centroid = centroid
        break
assert fcc_centroid is not None, "Could not find fcc hollow site"

hollow_dz = np.sqrt(max(0, d_PtO**2 - (d_PtPt / np.sqrt(3))**2))
hollow_z = z_surf + hollow_dz

# ----- Assemble structures and attach EMT -----
ontop_slab = slab.copy()
ontop_slab += Atoms('O', positions=[(ontop_pt[0], ontop_pt[1], ontop_z)])
ontop_slab += Atoms('H', positions=[(ontop_pt[0], ontop_pt[1], ontop_z + d_OH)])

bridge_slab = slab.copy()
bridge_slab += Atoms('O', positions=[(bridge_center[0], bridge_center[1], bridge_z)])
bridge_slab += Atoms('H', positions=[(bridge_center[0], bridge_center[1], bridge_z + d_OH)])

hollow_slab = slab.copy()
hollow_slab += Atoms('O', positions=[(fcc_centroid[0], fcc_centroid[1], hollow_z)])
hollow_slab += Atoms('H', positions=[(fcc_centroid[0], fcc_centroid[1], hollow_z + d_OH)])

for s in (ontop_slab, bridge_slab, hollow_slab):
    s.calc = EMT()

# ----- Single-point energies -----
e_ontop = ontop_slab.get_potential_energy()
e_bridge = bridge_slab.get_potential_energy()
e_hollow = hollow_slab.get_potential_energy()

energies = {'ontop': e_ontop, 'bridge': e_bridge, 'fcc hollow': e_hollow}
lowest = min(energies, key=energies.get)

print("Single-point energies (eV):")
for site, e in energies.items():
    print(f"  {site}: {e:.6f}")
print(f"The lowest energy site is {lowest}.")
