from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
sites = ['ontop', 'bridge', 'fcc']
energies = []

for site in sites:
    ads_slab = slab.copy()
    add_adsorbate(ads_slab, Atoms('OH', positions=[[0, 0, 0], [0, 0, 1.5]]), 2.0, site)
    ads_slab.calc = EMT()
    energies.append(ads_slab.get_potential_energy())

min_energy_site = sites[energies.index(min(energies))]
print(f'The most stable site is {min_energy_site} with energy {min(energies)} eV')
