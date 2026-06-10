from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase import Atoms

def create_slab_site(site, height=1.5):
    slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
    oh = Atoms('OH', positions=[(0, 0, 0), (0, 0, 0.97)])
    if site == 'ontop':
        add_adsorbate(slab, oh, height, 'ontop')
    elif site == 'bridge':
        add_adsorbate(slab, oh, height, 'bridge')
    elif site == 'fcc':
        add_adsorbate(slab, oh, height, 'fcc')
    slab.calc = EMT()
    return slab

sites = ['ontop', 'bridge', 'fcc']
energies = {site: create_slab_site(site).get_potential_energy() for site in sites}
min_site = min(energies, key=energies.get)

print(f"Energies: {energies}")
print(f"Lowest energy site: {min_site}")
