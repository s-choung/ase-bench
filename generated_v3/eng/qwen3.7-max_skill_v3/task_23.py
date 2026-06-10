from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

slab_base = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
oh = molecule('OH')

sites = ['ontop', 'bridge', 'hollow']
energies = {}

for site in sites:
    slab = slab_base.copy()
    add_adsorbate(slab, oh, height=2.0, position=site)
    slab.calc = EMT()
    energies[site] = slab.get_potential_energy()

for site, e in energies.items():
    print(f"{site:10s}: {e:.4f} eV")

best = min(energies, key=energies.get)
print(f"\nLowest energy adsorption site: {best} ({energies[best]:.4f} eV)")
