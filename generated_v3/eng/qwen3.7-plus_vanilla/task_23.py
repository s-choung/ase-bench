from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase import Atoms

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
oh = Atoms('OH', positions=[(0, 0, 0), (0, 0, 0.97)])

energies = {}
for site in ['ontop', 'bridge', 'fcc']:
    sys = slab.copy()
    add_adsorbate(sys, oh, height=1.5, position=site)
    sys.calc = EMT()
    energies[site] = sys.get_potential_energy()

best_site = min(energies, key=energies.get)
print(f"Energies: {energies}")
print(f"Lowest energy site: {best_site}")
