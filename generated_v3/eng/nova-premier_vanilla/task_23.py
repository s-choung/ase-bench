from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

# Create Pt(111) slab, 3 layers, (2x2) surface
slab = fcc111('Pt', size=(2,2,3), vacuum=10.0)

positions = ['ontop', 'bridge', 'fcc']
energies = {}

for pos in positions:
    # Copy slab and add OH adsorbate
    ads_slab = slab.copy()
    add_adsorbate(ads_slab, 'OH', height=1.5, position=pos)
    
    # Attach EMT calculator and compute energy
    ads_slab.calc = EMT()
    energies[pos] = ads_slab.get_potential_energy()

# Determine site with lowest energy
min_site = min(energies, key=energies.get)
print(f"Lowest energy site: {min_site}, Energy: {energies[min_site]}")
