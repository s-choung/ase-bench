from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
import numpy as np

# Create 3-layer Pt(111) slab
slab = fcc111('Pt', size=(4, 4, 3), vacuum=10.0, periodic=True)

# Prepare OH molecule
oh = molecule('OH')

# Sites to test
sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    atoms = slab.copy()
    add_adsorbate(atoms, oh, height=1.5, position=site)
    atoms.calc = EMT()
    e = atoms.get_potential_energy()
    energies[site] = e
    print(f'{site:6s} site: {e:.5f} eV')

# Find lowest energy site
lowest_site = min(energies, key=energies.get)
print(f'\nLowest energy site: {lowest_site} ({energies[lowest_site]:.5f} eV)')
