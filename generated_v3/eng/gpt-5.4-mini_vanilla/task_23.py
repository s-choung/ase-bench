from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Build Pt(111) 3-layer slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# OH adsorbate
oh = molecule('OH')

sites = {
    'ontop': (1.0, 1.0),
    'bridge': (1.5, 1.0),
    'fcc': (1.0, 1.5),
}

energies = {}

for site, pos in sites.items():
    atoms = slab.copy()
    add_adsorbate(atoms, oh, height=1.8, position=pos)
    atoms.calc = EMT()
    energies[site] = atoms.get_potential_energy()
    print(f'{site:6s}: {energies[site]:.6f} eV')

lowest_site = min(energies, key=energies.get)
print(f'\nLowest energy site: {lowest_site} ({energies[lowest_site]:.6f} eV)')
