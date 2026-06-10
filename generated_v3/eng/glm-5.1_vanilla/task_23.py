from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
oh = molecule('OH')

sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    system = slab.copy()
    add_adsorbate(system, oh, height=2.0, position=site)
    system.calc = EMT()
    energies[site] = system.get_potential_energy()

best_site = min(energies, key=energies.get)

print("Single-point energies (eV):")
for site, e in energies.items():
    print(f"  {site}: {e:.4f}")

print(f"\nLowest energy site: {best_site} ({energies[best_site]:.4f} eV)")
