from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT

a = 3.92
size = (2, 2, 3)
vacuum = 10.0
height = 1.85

sites = ["ontop", "bridge", "fcc"]
energies = {}

for site in sites:
    slab = fcc111("Pt", size=size, a=a, vacuum=vacuum)
    oh = molecule("OH")
    add_adsorbate(slab, oh, height=height, position=site)
    slab.calc = EMT()
    energies[site] = slab.get_potential_energy()

for site in sites:
    print(f"{site:6s}: {energies[site]:.6f} eV")

best = min(energies, key=energies.get)
print(f"Lowest-energy site: {best} ({energies[best]:.6f} eV)")
