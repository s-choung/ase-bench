from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

# Create Pt(111) slab with 3 layers and vacuum
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
oh = Atoms('OH', positions=[(0, 0, 0), (0, 0, 0.96)])

sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    ads_slab = slab.copy()
    add_adsorbate(ads_slab, oh, height=1.8, position=site)
    ads_slab.calc = EMT()
    energies[site] = ads_slab.get_potential_energy()

min_site = min(energies, key=energies.get)
print(f"Lowest energy site: {min_site} with energy {energies[min_site]:.4f} eV")
