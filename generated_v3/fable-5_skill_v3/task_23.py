from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

sites = ['ontop', 'bridge', 'fcc']
results = {}

for site in sites:
    slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
    oh = molecule('OH')
    add_adsorbate(slab, oh, height=2.0, position=site)
    slab.calc = EMT()
    e = slab.get_potential_energy()
    results[site] = e
    print(f"{site:8s}: {e:.4f} eV")

best = min(results, key=results.get)
print(f"\n가장 낮은 에너지 사이트: {best} ({results[best]:.4f} eV)")
