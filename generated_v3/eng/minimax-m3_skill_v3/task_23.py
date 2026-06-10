from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
import numpy as np

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
z_vals = np.unique(np.round(slab.positions[:, 2], 2))
z_2nd = z_vals[-2]

oh = Atoms('OH', positions=[(0, 0, 0), (0, 0, 0.98)])

results = {}
for site in ['ontop', 'bridge', 'fcc']:
    s = slab.copy()
    add_adsorbate(s, oh, height=2.0, position=site)
    s.set_constraint(FixAtoms(mask=s.positions[:, 2] < z_2nd + 0.1))
    s.calc = EMT()
    results[site] = s.get_potential_energy()

for site, e in results.items():
    print(f"{site:8s}: {e:.4f} eV")
best = min(results, key=results.get)
print(f"\nLowest energy site: {best}")
