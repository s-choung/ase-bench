from ase.build import fcc111, add_adsorbate
from ase import Atoms
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
oh = Atoms('OH', positions=[[0, 0, 0], [0, 0, 0.97]])

sites = [('ontop', (0, 0)), ('bridge', (0.5, 0)), ('fcc', (1/3, 1/3))]
energies = {}

for name, pos in sites:
    atoms = slab.copy()
    atoms.calc = EMT()
    add_adsorbate(atoms, oh, height=1.5, position=pos)
    energies[name] = atoms.get_potential_energy()

for name, e in energies.items():
    print(f"{name}: {e:.3f} eV")

print(f"Lowest energy site: {min(energies, key=energies.get)}")
