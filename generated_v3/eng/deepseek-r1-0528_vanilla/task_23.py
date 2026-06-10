from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(3,3,3), vacuum=10.0)
oh = Atoms('OH', positions=[[0, 0, 0], [0, 0, 1.0]])
sites = ['ontop', 'bridge', 'fcc']
systems = []

for site in sites:
    slab_copy = slab.copy()
    add_adsorbate(slab_copy, oh, height=1.5, position=site, offset=(0.5,0.5))
    systems.append((site, slab_copy))

energies = []
for site, system in systems:
    system.calc = EMT()
    e = system.get_potential_energy()
    energies.append((e, site))

energies.sort()
min_energy = energies[0][0]
min_site = energies[0][1]

for e, site in energies:
    print(f"{site}: {e:.3f} eV")
print(f"The most stable adsorption site is {min_site}.")
