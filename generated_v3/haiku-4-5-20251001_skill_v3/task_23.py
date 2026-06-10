from ase.build import fcc111, add_adsorbate, add_vacuum
from ase.build import molecule
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)

oh = molecule('OH')

sites = ['ontop', 'bridge', 'fcc']
structures = {}
energies = {}

for site in sites:
    atoms = slab.copy()
    ads = oh.copy()
    add_adsorbate(atoms, ads, height=1.8, position=site)
    atoms.calc = EMT()
    e = atoms.get_potential_energy()
    structures[site] = atoms
    energies[site] = e

print("Single-point energies (eV):")
for site in sites:
    print(f"  {site:10s}: {energies[site]:10.6f}")

min_site = min(energies, key=energies.get)
print(f"\nLowest energy site: {min_site} ({energies[min_site]:.6f} eV)")
