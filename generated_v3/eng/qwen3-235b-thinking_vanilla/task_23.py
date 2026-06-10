from ase import Atom
from ase.build import fcc111
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0, orthogonal=True)
top_positions = slab.positions[-4:]
height, oh_bond = 1.8, 0.96
energies, sites = [], ['ontop', 'bridge', 'fcc']

for site in sites:
    ads_slab = slab.copy()
    if site == 'ontop':
        O_pos = top_positions[0].copy()
        O_pos[2] += height
        ads_slab += [Atom('O', O_pos), Atom('H', O_pos + [0, 0, oh_bond])]
    elif site == 'bridge':
        O_pos = (top_positions[0] + top_positions[1]) / 2
        O_pos[2] = top_positions[0][2] + height
        ads_slab += [Atom('O', O_pos), Atom('H', O_pos + [0, 0, oh_bond])]
    else:
        O_pos = (top_positions[0] + top_positions[1] + top_positions[2]) / 3
        O_pos[2] = top_positions[0][2] + height
        ads_slab += [Atom('O', O_pos), Atom('H', O_pos + [0, 0, oh_bond])]
    ads_slab.calc = EMT()
    energies.append(ads_slab.get_potential_energy())

min_idx = energies.index(min(energies))
print(f"Lowest energy site: {sites[min_idx]}")
