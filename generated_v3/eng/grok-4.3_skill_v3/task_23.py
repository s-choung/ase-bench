from ase import Atoms
from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

def make_ads(site):
    slab = fcc111('Pt', size=(2,2,3), vacuum=10.0)
    oh = molecule('OH')
    add_adsorbate(slab, oh, height=1.8, position=site)
    slab.calc = EMT()
    return slab.get_potential_energy(), site

energies = [make_ads(s) for s in ['ontop', 'bridge', 'fcc']]
min_e, min_site = min(energies)
print(f"Lowest energy: {min_site} ({min_e:.4f} eV)")
