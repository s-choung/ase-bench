from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

# Prepare slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# Site positions: find first top, bridge, fcc
ontop = slab[0].position[:2]  # top of atom 0
bridge = 0.5 * (slab[0].position[:2] + slab[1].position[:2])  # between atom 0 and 1
# Find one fcc hollow (use triangle of first 3 atoms)
fcc = (slab[0].position[:2] + slab[1].position[:2] + slab[3].position[:2]) / 3

site_names = ['ontop', 'bridge', 'fcc']
site_positions = [ontop, bridge, fcc]
energies = []

for name, pos in zip(site_names, site_positions):
    s = slab.copy()
    oh = molecule('OH')
    add_adsorbate(s, oh, height=1.9, position=pos)
    s.calc = EMT()
    e = s.get_potential_energy()
    energies.append(e)
    print(f'{name}: {e:.6f} eV')

minidx = energies.index(min(energies))
print(f'Lowest energy site: {site_names[minidx]} ({energies[minidx]:.6f} eV)')
