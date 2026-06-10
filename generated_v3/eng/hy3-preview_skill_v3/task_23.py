from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

# Build 3-layer Pt(111) slab with 10 Å vacuum
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# Create OH adsorbate
oh = molecule('OH')

# Define adsorption sites
sites = ['ontop', 'bridge', 'fcc']
energies = {}

# Compute single-point energy for each site
for site in sites:
    slab_copy = slab.copy()
    add_adsorbate(slab_copy, oh, height=2.0, position=site)
    slab_copy.calc = EMT()
    energies[site] = slab_copy.get_potential_energy()

# Find and report lowest energy site
min_site = min(energies, key=energies.get)
print(f"Energies: {energies}")
print(f"Lowest energy site: {min_site} ({energies[min_site]:.4f} eV)")
