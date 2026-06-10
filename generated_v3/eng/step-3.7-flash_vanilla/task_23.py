from ase import Atoms
from ase.build import bulk, surface
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
import numpy as np

# Build 3-layer 2x2 Pt(111) slab with 10Å vacuum
a = 3.92  # Pt lattice constant (Å)
slab = surface(bulk('Pt', 'fcc', a=a), (111), layers=3, vacuum=10, size=(2,2,1))
slab.set_constraint(FixAtoms(slab.positions[:,2] < slab.positions[:,2].min() + 1))

# Get surface Pt positions and compute adsorption sites
top_z = slab.positions[:,2].max()
surf = np.array([a.position for a in slab if a.symbol == 'Pt' and abs(a.z - top_z) < 0.5])[:,:2]
d = a / np.sqrt(2)  # Nearest neighbor distance on Pt(111)
dist = np.linalg.norm(surf[:,None] - surf[None,:], axis=2)

# Bridge site (midpoint of adjacent Pt pair)
bp = np.argwhere(np.abs(dist - d) < 0.1)[0]
bridge_pos = (surf[bp[0]] + surf[bp[1]]) / 2

# FCC hollow site (centroid of adjacent Pt triplet)
for i in range(len(surf)):
    for j in range(i+1, len(surf)):
        if abs(dist[i,j] - d) < 0.1:
            for k in range(j+1, len(surf)):
                if abs(dist[i,k]-d) < 0.1 and abs(dist[j,k]-d) < 0.1:
                    fcc_pos = surf[[i,j,k]].mean(0)
                    break
            else: continue
            break
    else: continue
    break
ontop_pos = surf[0]

# OH adsorbate (O at origin, H along +z axis)
oh = Atoms('OH', positions=[[0,0,0],[0,0,0.96]])
h = 1.0  # O height above surface Pt (Å)

# Calculate single-point energies for each site
e = {}
for site, pos in [('ontop', ontop_pos), ('bridge', bridge_pos), ('fcc', fcc_pos)]:
    s = slab.copy()
    o_pos = np.append(pos, top_z + h)
    s += oh.copy().translate(o_pos)
    s.calc = EMT()
    e[site] = s.get_potential_energy()

# Output results
for site, val in e.items():
    print(f"{site.capitalize()}: {val:.3f} eV")
best = min(e, key=e.get)
print(f"\nMost stable site: {best} ({e[best]:.3f} eV)")
