from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT

# Pt(111) slab, 3 layers, 2×2 surface cell, 10 Å vacuum
base_slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

sites = ['ontop', 'bridge', 'fcc']     # adsorption sites to test
energies = {}

for site in sites:
    slab = base_slab.copy()            # independent slab for each site
    oh = molecule('OH')                # OH adsorbate
    add_adsorbate(slab, oh, height=1.5, position=site)  # in‑place modification
    slab.calc = EMT()                  # attach built‑in calculator
    energies[site] = slab.get_potential_energy()
    print(f'{site:5s} energy = {energies[site]:.6f} eV')

lowest = min(energies, key=energies.get)
print(f'\nLowest‑energy site: {lowest} ({energies[lowest]:.6f} eV)')
