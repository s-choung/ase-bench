from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

sites = ['ontop', 'bridge', 'hollow']
results = {}

for site in sites:
    slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
    oh = molecule('OH')
    # add_adsorbate modifies slab in-place
    add_adsorbate(slab, oh, height=1.8, position=site)
    slab.calc = EMT()
    results[site] = slab.get_potential_energy()

best_site = min(results, key=results.get)

for site, energy in results.items():
    print(f"{site}: {energy:.4f} eV")

print(f"Lowest energy site: {best_site}")
