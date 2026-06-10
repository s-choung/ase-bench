from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT
from ase import Atoms
import numpy as np

# Create Pt(111) 3-layer slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# OH molecule (bond length ~0.96 Å)
oh = Atoms('OH', positions=[(0, 0, 0), (0, 0, 0.96)])

sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    atoms = slab.copy()
    add_adsorbate(atoms, oh, height=2.0, position=site)
    atoms.calc = EMT()
    energies[site] = atoms.get_potential_energy()
    print(f"{site}: {energies[site]:.4f} eV")

lowest = min(energies, key=energies.get)
print(f"\nLowest energy site: {lowest} ({energies[lowest]:.4f} eV)")
