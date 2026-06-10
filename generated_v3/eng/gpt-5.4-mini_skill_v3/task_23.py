from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT

sites = ["ontop", "bridge", "fcc"]
energies = {}

for site in sites:
    slab = fcc111("Pt", size=(2, 2, 3), vacuum=10.0)
    oh = molecule("OH")
    add_adsorbate(slab, oh, height=1.8, position=site)
    slab.calc = EMT()
    energies[site] = slab.get_potential_energy()
    print(f"{site:6s}: {energies[site]:.6f} eV")

best_site = min(energies, key=energies.get)
print(f"Lowest energy site: {best_site} ({energies[best_site]:.6f} eV)")
