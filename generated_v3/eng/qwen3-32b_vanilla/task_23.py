from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase import Atoms

slab = fcc111('Pt', (3, 3, 3), vacuum=8.0)
oh = Atoms('OH', positions=[(0, 0, 0), (0, 0, 1.0)])

slab_ontop = slab.copy()
add_adsorbate(slab_ontop, oh, 1.5, 'ontop')

slab_bridge = slab.copy()
add_adsorbate(slab_bridge, oh, 1.5, 'bridge')

slab_fcc = slab.copy()
add_adsorbate(slab_fcc, oh, 1.5, 'fcc')

for s in [slab_ontop, slab_bridge, slab_fcc]:
    s.calc = EMT()

e_ontop = slab_ontop.get_potential_energy()
e_bridge = slab_bridge.get_potential_energy()
e_fcc = slab_fcc.get_potential_energy()

sites = [('ontop', e_ontop), ('bridge', e_bridge), ('fcc', e_fcc)]
sites.sort(key=lambda x: x[1])
print(f"Lowest energy site: {sites[0][0]}")
