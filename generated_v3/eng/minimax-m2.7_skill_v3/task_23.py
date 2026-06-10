from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase import Atoms

slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
oh = Atoms('OH', positions=[(0, 0, 0), (0, 0, 1.0)])

sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    atoms = slab.copy()
    add_adsorbate(atoms, oh, height=1.8, position=site)
    atoms.calc = EMT()
    energies[site] = atoms.get_potential_energy()
    print(f"{site}: {energies[site]:.4f} eV")

best = min(energies, key=energies.get)
print(f"\nLowest energy site: {best} ({energies[best]:.4f} eV)")
