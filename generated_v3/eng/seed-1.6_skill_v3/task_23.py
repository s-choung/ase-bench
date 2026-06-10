from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

# Build Pt(111) 3-layer slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
oh = molecule('OH')

# Prepare slabs for each adsorption site
sites = {'ontop': (0.0, 0.0), 'bridge': (0.5, 0.0), 'fcc': (1/3, 1/3)}
energies = {}

for site, pos in sites.items():
    slab_copy = slab.copy()
    add_adsorbate(slab_copy, oh, height=1.8, position=pos)
    slab_copy.calc = EMT()
    energies[site] = slab_copy.get_potential_energy()

# Find and print lowest energy site
lowest_site = min(energies, key=energies.get)
print(f'Lowest energy site: {lowest_site} (energy: {energies[lowest_site]:.4f} eV)')
