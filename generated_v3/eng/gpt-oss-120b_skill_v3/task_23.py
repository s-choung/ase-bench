from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
import numpy as np

# base Pt(111) slab, 3 layers, 2x2 surface, 10 Å vacuum
base_slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    slab = base_slab.copy()                     # independent slab
    oh = molecule('OH')                         # OH adsorbate
    add_adsorbate(slab, oh, height=1.5, position=site)  # in‑place
    slab.calc = EMT()
    energies[site] = slab.get_potential_energy()

# report
for site, e in energies.items():
    print(f"{site:6s} site energy = {e: .6f} eV")
best = min(energies, key=energies.get)
print(f"\nLowest energy: {best} site ({energies[best]: .6f} eV)")
