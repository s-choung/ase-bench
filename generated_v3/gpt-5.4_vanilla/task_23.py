from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT

sites = [('ontop', 'ontop'), ('bridge', 'bridge'), ('fcc', 'fcc')]
results = {}

for label, site in sites:
    slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
    oh = molecule('OH')
    add_adsorbate(slab, oh, height=1.9, position=site)
    slab.calc = EMT()
    e = slab.get_potential_energy()
    results[label] = e
    print(f'{label}: {e:.6f} eV')

best = min(results, key=results.get)
print(f'lowest_energy_site: {best} ({results[best]:.6f} eV)')
