from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
oh = molecule('OH')
energies = {}

for site in ['ontop', 'bridge', 'fcc']:
    s = slab.copy()
    add_adsorbate(s, oh, height=2.0, position=site)
    s.calc = EMT()
    energies[site] = s.get_potential_energy()

for site, e in energies.items():
    print(f"{site:10s}: {e:8.3f} eV")

best = min(energies, key=energies.get)
print(f"\nLowest energy site: {best} ({energies[best]:.3f} eV)")
