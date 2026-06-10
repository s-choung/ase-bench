from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
slab = fcc111('Pt', (2, 2, 3), vacuum=10.0)
sites = ['ontop', 'bridge', 'fcc']
energies = {}
for site in sites:
    s = slab.copy()
    mol = Atoms('OH', [(0, 0, 0), (0, 0, 0.97)])
    add_adsorbate(s, mol, 1.8, site)
    s.calc = EMT()
    energies[site] = s.get_potential_energy()
min_site = min(energies, key=energies.get)
print(min_site, energies[min_site])
