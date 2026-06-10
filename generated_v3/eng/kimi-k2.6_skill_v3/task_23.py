from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

base = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
oh = molecule('OH')
sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    slab = base.copy()
    add_adsorbate(slab, oh, height=2.0, position=site)
    slab.calc = EMT()
    energies[site] = slab.get_potential_energy()

lowest = min(energies, key=energies.get)
print(f"Energies: {energies}")
print(f"Lowest energy site: {lowest} ({energies[lowest]:.4f} eV)")
