from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase import Atoms

slab = fcc111('Pt', size=(1, 1, 3), vacuum=10.0)
slab.calc = EMT()

sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    atoms = slab.copy()
    oh = molecule('OH')
    add_adsorbate(atoms, oh, height=1.8, position=site)
    atoms.calc = EMT()
    atoms.center(vacuum=10.0, axis=2)
    energy = atoms.get_potential_energy()
    energies[site] = energy
    print(f'{site}: {energy:.4f} eV')

best = min(energies, key=energies.get)
print(f'Lowest energy site: {best} ({energies[best]:.4f} eV)')
