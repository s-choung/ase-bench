from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

# Create base 3-layer Pt(111) slab with sufficient vacuum
base_slab = fcc111('Pt', size=(3,3,3), vacuum=15.0, a=3.92)
adsorption_sites = ['ontop', 'bridge', 'fcc']
energies = {}

# Calculate single-point energy for each adsorption site
for site in adsorption_sites:
    slab = base_slab.copy()
    oh = molecule('OH')
    add_adsorbate(slab, oh, height=2.0, position=site)
    slab.calc = EMT()
    energies[site] = slab.get_potential_energy()

# Print results and find lowest energy site
print("Adsorption site energies (eV):")
for site, e in energies.items():
    print(f"{site:>6}: {e:.3f}")

lowest_site = min(energies, key=energies.get)
print(f"\nLowest energy site: {lowest_site} (E = {energies[lowest_site]:.3f} eV)")
