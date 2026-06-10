from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
oh = molecule('OH')
sites = ['ontop', 'bridge', 'fcc']
energies = {}
for site in sites:
    at = slab.copy()
    add_adsorbate(at, oh, height=1.5, position=site)
    at.calc = EMT()
    energies[site] = at.get_potential_energy()
print(min(energies, key=energies.get))
