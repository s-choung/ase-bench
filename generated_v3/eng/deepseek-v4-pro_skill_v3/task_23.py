from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

# Create Pt(111) 3-layer slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
oh = molecule('OH')

sites = {
    'ontop': 'ontop',
    'bridge': 'bridge',
    'fcc': 'fcc'
}

energies = {}

for name, site in sites.items():
    atoms = slab.copy()
    add_adsorbate(atoms, oh, height=1.8, position=site)
    atoms.calc = EMT()
    energies[name] = atoms.get_potential_energy()

for name, e in energies.items():
    print(f"{name}: {e:.3f} eV")

best_site = min(energies, key=energies.get)
print(f"\nLowest energy site: {best_site} ({energies[best_site]:.3f} eV)")
