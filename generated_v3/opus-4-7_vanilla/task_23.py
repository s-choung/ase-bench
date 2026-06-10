from ase.build import fcc111, add_adsorbate
from ase.atoms import Atoms
from ase.calculators.emt import EMT
import numpy as np

def make_oh():
    return Atoms('OH', positions=[[0,0,0],[0,0,0.97]])

sites = ['ontop', 'bridge', 'fcc']
results = {}

for site in sites:
    slab = fcc111('Pt', size=(3,3,3), vacuum=10.0)
    oh = make_oh()
    add_adsorbate(slab, oh, height=2.0, position=site)
    slab.calc = EMT()
    e = slab.get_potential_energy()
    results[site] = e
    print(f"{site}: {e:.4f} eV")

best = min(results, key=results.get)
print(f"Lowest energy site: {best} ({results[best]:.4f} eV)")
