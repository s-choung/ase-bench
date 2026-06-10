from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

# Create clean Pt(111) slab: 2x2 surface, 3 layers
slab = fcc111('Pt', size=(2, 2, 3), a=3.92)

# Create OH molecule (O at origin, H along z)
oh = Atoms('OH', positions=[(0, 0, 0), (0, 0, 0.97)])

sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    copy = slab.copy()
    add_adsorbate(copy, oh, height=1.8, position=site)
    copy.calc = EMT()
    energies[site] = copy.get_potential_energy()
    print(f'{site}: {energies[site]:.3f} eV')

best = min(energies, key=energies.get)
print(f'\nLowest energy site: {best} with {energies[best]:.3f} eV')
