from ase.build import fcc111, add_adsorbate, surface_sites
from ase import Atoms
from ase.calculators.emt import EMT
import copy

# Pt(111) slab: 2×2 surface, 3 layers, 10 Å vacuum
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# adsorption sites
sites = surface_sites(slab)

# OH molecule (O lower, H above)
OH = Atoms('OH', positions=[[0, 0, 0], [0, 0, 0.97]])

height = 1.6  # O‑surface distance (Å)
energies = {}

for site in ['ontop', 'bridge', 'fcc']:
    s = copy.deepcopy(slab)
    add_adsorbate(s, OH, height, sites[site][0][:2])  # place OH
    s.set_calculator(EMT())
    energies[site] = s.get_potential_energy()

lowest = min(energies, key=energies.get)

for site, e in energies.items():
    print(f'{site}: {e:.3f} eV')
print(f'Lowest energy site: {lowest}')
