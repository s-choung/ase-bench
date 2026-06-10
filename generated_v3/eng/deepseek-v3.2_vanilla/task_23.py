from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
import numpy as np

# Create Pt(111) slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
slab.calc = EMT()
E_slab = slab.get_potential_energy()

# Define adsorption sites relative to slab cell
positions = {
    'ontop': (0.5, 0.5, 0),
    'bridge': (0.0, 0.5, 0),
    'fcc': (1/3, 1/3, 0)
}

results = {}
for site, pos in positions.items():
    slab_copy = slab.copy()
    # Place OH molecule (O above H)
    add_adsorbate(slab_copy, 'O', height=1.5, position=pos)
    # Add H atom bonded to O
    o_pos = slab_copy[-1].position
    h_pos = o_pos + [0, 0, 0.98]
    slab_copy += Atoms('H', positions=[h_pos])
    
    slab_copy.calc = EMT()
    E_total = slab_copy.get_potential_energy()
    E_ads = E_total - E_slab - Atoms('OH', positions=[[0,0,0],[0,0,0.98]]).get_potential_energy()
    results[site] = E_ads

lowest_site = min(results, key=results.get)
print(f'Adsorption energies (eV): {results}')
print(f'Lowest energy site: {lowest_site}')
