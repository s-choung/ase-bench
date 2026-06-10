from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
import numpy as np

# Create 3-layer Pt(111) slab (3x3 supercell)
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)

# Define adsorption sites
sites = {
    'ontop': (0.0, 0.0),
    'bridge': (0.5, 0.0),
    'fcc': (1/3, 1/3)
}

energies = {}
for name, (x, y) in sites.items():
    # Deep copy slab
    ads_slab = slab.copy()
    # Add OH at specified site (height ~1.5 Å above surface)
    add_adsorbate(ads_slab, 'OH', height=1.5, position=(x*ads_slab.cell[0,0] + y*ads_slab.cell[1,0], 
                                                      x*ads_slab.cell[0,1] + y*ads_slab.cell[1,1]))
    # Attach EMT calculator and compute energy
    ads_slab.calc = EMT()
    energies[name] = ads_slab.get_potential_energy()

# Find and print lowest energy site
lowest_site = min(energies, key=energies.get)
print(f"Lowest energy site: {lowest_site} ({energies[lowest_site]:.3f} eV)")
