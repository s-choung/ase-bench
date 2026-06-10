from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase import Atoms

sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
    oh = Atoms('OH', positions=[(0, 0, 0), (0, 0, 0.97)])
    add_adsorbate(slab, oh, height=2.0, position=site)
    slab.calc = EMT()
    energies[site] = slab.get_potential_energy()

for site in sites:
    print(f'{site:>6}: {energies[site]:.6f} eV')

best_site = min(energies, key=energies.get)
print(f'Lowest-energy site: {best_site} ({energies[best_site]:.6f} eV)')
