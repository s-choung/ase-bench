from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

slab_base = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
oh = molecule('OH')
sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    atoms = slab_base.copy()
    add_adsorbate(atoms, oh.copy(), height=1.5, position=site)
    atoms.calc = EMT()
    energies[site] = atoms.get_potential_energy()

best_site = min(energies, key=energies.get)

print("Adsorption Site Energies (eV):")
for site, energy in energies.items():
    print(f"  {site:7s}: {energy:.4f}")
print(f"\nLowest energy site: {best_site} ({energies[best_site]:.4f} eV)")
