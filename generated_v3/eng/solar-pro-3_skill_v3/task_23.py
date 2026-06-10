from ase import Atoms
from ase.build import fcc111
from ase.build import add_adsorbate
from ase.calculators.emt import EMT


# bulk reference (7‑layer)
Pt = fcc111('Pt', size=(2, 2, 7), vacuum=15.0)   # vacuum enough for free adsorption
Pt.set_calculator(EMT())

# positions for the three sites on a (2×2) surface
ontop = [(0, 0, 0)]
bridge = [(1/3, 1/3, 0)]
hollow = [(1/2, 0, 0)]

energies = {}

for name, pos in [('ontop', ontop), ('bridge', bridge), ('hollow', hollow)]:
    slab = Pt.copy()
    # add the OH adsorbate (ontop → on top, bridge → adatom bridge, hollow → fcc site)
    add_adsorbate(slab, 'OH', height=1.2, position=pos)
    # set the calculator already present in the original atom (EMT)
    energies[name] = slab.get_potential_energy()

print('Site energies (eV):')
for name, e in energies.items():
    print(f'{name:>8}: {e:.6f}')
lowest = min(energies, key=energies.get)
lowest_energy = energies[lowest]
print(f'\nLowest site: {lowest} with energy {lowest_energy:.6f} eV')
