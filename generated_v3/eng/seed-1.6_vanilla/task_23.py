from ase import Atoms
from ase.build import surface
from ase.calculators.emt import EMT

# Create Pt(111) 3-layer slab
slab = surface('Pt', (1,1,1), size=(2,2,3), vacuum=10.0)
ads_sites, site_labels = slab.get_adsorption_sites()
target_sites = ['ontop', 'bridge', 'fcc']
selected_pos = [ads_sites[site_labels.index(s)] for s in target_sites]

# Compute energies for each adsorption site
site_energies = {}
for site, pos in zip(target_sites, selected_pos):
    struct = slab.copy()
    struct += Atoms('O', positions=[pos])
    struct += Atoms('H', positions=[(pos[0], pos[1], pos[2] + 0.96)])
    struct.calc = EMT()
    site_energies[site] = struct.get_potential_energy()

# Find and print lowest energy site
min_site = min(site_energies, key=site_energies.get)
print(f"Lowest energy site: {min_site} (energy: {site_energies[min_site]:.2f} eV)")
