from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

slab_base = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
oh = molecule('OH')

sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    slab = slab_base.copy()
    add_adsorbate(slab, oh, height=1.5, position=site)
    slab.calc = EMT()
    E = slab.get_potential_energy()
    energies[site] = E
    print(f'Site: {site:<7} | Energy: {E:.4f} eV')

min_site = min(energies, key=energies.get)
print(f'\nLowest energy site: {min_site} ({energies[min_site]:.4f} eV)')
