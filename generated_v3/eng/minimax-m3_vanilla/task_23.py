from ase.build import fcc111, add_adsorbate
from ase import Atoms
from ase.calculators.emt import EMT

a = 3.92
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0, a=a)

oh = Atoms('OH', positions=[(0, 0, 0), (0, 0, 0.97)])

sites = [
    ('ontop',  2.0),
    ('bridge', 1.8),
    ('fcc',    1.6),
]

energies = {}
for name, height in sites:
    s = slab.copy()
    add_adsorbate(s, oh, name, height)
    s.calc = EMT()
    energies[name] = s.get_potential_energy()

for name, e in energies.items():
    print(f"{name}: {e:.4f} eV")

min_site = min(energies, key=energies.get)
print(f"\nLowest energy: {min_site} ({energies[min_site]:.4f} eV)")
