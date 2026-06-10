from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT

sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
    oh = molecule('OH')
    add_adsorbate(slab, oh, height=2.0, position=site)
    slab.calc = EMT()
    energies[site] = slab.get_potential_energy()

for site, e in energies.items():
    print(f"{site:8s}: {e:.4f} eV")

best = min(energies, key=energies.get)
print(f"\nLowest energy site: {best} ({energies[best]:.4f} eV)")
