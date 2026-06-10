import numpy as np
from ase import Atom
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, a=3.61)
tags = slab.get_tags()
top = np.where(tags == tags.max())[0]

i0 = top[0]
mind, i1 = 1e9, None
for j in top:
    if j == i0:
        continue
    d = slab.get_distance(i0, j, mic=True)
    if d < mind:
        mind = d
        i1 = j

p0 = slab.positions[i0]
v = slab.get_distance(i0, i1, vector=True)

def rot(v_, ang):
    a = np.deg2rad(ang)
    c, s = np.cos(a), np.sin(a)
    return np.array([v_[0]*c - v_[1]*s, v_[0]*s + v_[1]*c, 0.0])

sites = [p0[:2] + (v[:2] + rot(v, sign)[:2]) / 3 for sign in (60, -60)]
z = np.max(slab.positions[:, 2]) + 1.8

states = []
for xy in sites:
    s = slab.copy()
    s.append(Atom('Cu', [xy[0], xy[1], z]))
    s.set_constraint(FixAtoms(indices=range(len(slab))))
    s.calc = EMT()
    BFGS(s).run(fmax=0.01)
    states.append(s)

if states[0].get_potential_energy() > states[1].get_potential_energy():
    initial, final = states[1], states[0]
else:
    initial, final = states[0], states[1]

images = [initial] + [initial.copy() for _ in range(5)] + [final]
neb = NEB(images)
neb.interpolate(method='idpp')

for img in images[1:-1]:
    img.calc = EMT()

BFGS(neb).run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.3f} eV")
