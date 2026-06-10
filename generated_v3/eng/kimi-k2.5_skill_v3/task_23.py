from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

slab_base = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
oh = molecule('OH')
sites = ['ontop', 'bridge', 'hollow']
results = []

for site in sites:
    slab = slab_base.copy()
    add_adsorbate(slab, oh, height=1.8, position=site)
    slab.calc = EMT()
    energy = slab.get_potential_energy()
    results.append((site, energy))
    print(f"{site:10s}: {energy:10.3f} eV")

min_site, min_energy = min(results, key=lambda x: x[1])
print(f"\nLowest energy site: {min_site} ({min_energy:.3f} eV)")
