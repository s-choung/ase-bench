from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
oh = molecule('OH')
sites = ['ontop', 'bridge', 'hollow']

energies = {}
for site in sites:
    atoms = slab.copy()
    add_adsorbate(atoms, oh, 2.0, site)
    atoms.calc = EMT()
    energies[site] = atoms.get_potential_energy()

best = min(energies, key=energies.get)
for site, e in energies.items():
    print(f'{site:>10s}: {e:.4f} eV')
print(f'Lowest energy site: {best} ({energies[best]:.4f} eV)')
