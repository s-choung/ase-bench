from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase import Atoms

oh = Atoms('OH', positions=[[0, 0, 0], [0, 0, 0.97]])
sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
    add_adsorbate(slab, oh, height=2.0, position=site)
    slab.calc = EMT()
    energies[site] = slab.get_potential_energy()

best_site = min(energies, key=energies.get)
for site, e in energies.items():
    print(f"{site}: {e:.3f} eV")
print(f"Lowest energy site: {best_site}")
