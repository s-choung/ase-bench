from ase.build import fcc111, molecule
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
# import units only to specify pbc if needed
from ase import Atoms
import numpy as np

# bulk properties
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)   # 3‑layer Pt(111) slab
calc = EMT()
slab.calc = calc

# adsorb CO above the hollow site of the surface (h=1.8 Å)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='hollow')

# tag bottom two Pt layers for immobilization
tags = [p.tag for p in slab]
slab.set_tags(np.zeros(len(slab), dtype=int))
for i, p in enumerate(slab):
    dirz = np.array([0, 0, 1])
    normal = np.sum(dirz * p.position)
    slab.set_tags(i, tags[i] if normal < -0.5 else 0)

# fix the two bottom Pt layers
bottom_mask = np.zeros(len(slab), dtype=bool)
for i, p in enumerate(slab):
    if tags[i] > 0:
        bottom_mask[i] = True
slab.set_constraint(FixAtoms(mask=bottom_mask))

# store C atom index for bond‑length constraint
co_idx, pt_idx = [], []
for i, p in enumerate(slab):
    if str(p.symbol) == 'C':
        co_idx.append(i)
    elif str(p.symbol) == 'Pt':
        pt_idx.append(i)
pt_idx = sorted(pt_idx)[:2]   # first two bottom Pt atoms

# fix C–O distance
slab.set_constraint(FixBondLength(co_idx[0], pt_idx[1]))

# initial velocities for thermostated MD (optional but recommended)
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
distances = np.linalg.norm(slab[co_idx[0]].position - np.mean(slab[pt_idx].position, axis=0))  # Å
timescale = units.fs
dist_temp = distances * units.Ang
MC = MaxwellBoltzmannDistribution(slab, temperature_K=300)
MC.set_temperature(dist_temp)
# DRIFT BOTH TRANSLATIONAL & ROTATIONAL modes
Stationary(slab)

# BFGS optimization with fmax·0.05 eV/Å
opt = BFGS(slab)
opt.run(fmax=0.05)

# print final quantities
print('Final energy  : {:.4f} eV'.format(slab.get_potential_energy()))
print('C‑O distance : {:.4f} Å'.format(distances))
