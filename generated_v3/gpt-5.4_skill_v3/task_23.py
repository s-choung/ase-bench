from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase import Atoms

sites = {'ontop': 'ontop', 'bridge': 'bridge', 'fcc': 'fcc'}
results = {}

for name, pos in sites.items():
    slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
    oh = Atoms('OH', positions=[(0, 0, 0), (0, 0, 0.97)])
    add_adsorbate(slab, oh, height=1.8, position=pos)
    slab.calc = EMT()
    e = slab.get_potential_energy()
    results[name] = e
    print(f'{name}: {e:.6f} eV')

best = min(results, key=results.get)
print(f'lowest-energy site: {best} ({results[best]:.6f} eV)')
