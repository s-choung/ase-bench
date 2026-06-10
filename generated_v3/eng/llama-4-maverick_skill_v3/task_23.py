from ase import Atoms
from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(2,2,3), vacuum=10.0)

sites = ['ontop', 'bridge', 'fcc']
energies = []

for site in sites:
    slab_copy = slab.copy()
    oh = molecule('OH')
    add_adsorbate(slab_copy, oh, height=1.8, position=site)
    slab_copy.calc = EMT()
    energies.append(slab_copy.get_potential_energy())

min_energy = min(energies)
min_site = sites[energies.index(min_energy)]

print(f'Energies: {dict(zip(sites, energies))}')
print(f'Lowest energy site: {min_site} ({min_energy:.4f} eV)')
