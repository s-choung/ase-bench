from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase import Atoms

slab = fcc111('Pt', size=(1, 1, 3), vacuum=10.0)
oh = Atoms('OH', positions=[[0, 0, 0], [0, 0, 0.97]])

sites = {'ontop': (0.0, 0.0), 'bridge': (0.5, 0.0), 'fcc': (1/3, 1/3)}
energies = {}

for name, pos in sites.items():
    s = slab.copy()
    add_adsorbate(s, oh, height=1.5, position=pos)
    s.calc = EMT()
    energies[name] = s.get_potential_energy()

min_site = min(energies, key=energies.get)

for site, e in energies.items():
    print(f"{site.capitalize()}: {e:.3f} eV")
print(f"Lowest energy site: {min_site}")
