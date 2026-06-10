from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.io import write

sites = ["ontop", "bridge", "fcc"]
energies = {}

for site in sites:
    slab = fcc111("Pt", size=(3, 3, 3), vacuum=10.0)
    oh = Atoms("OH", positions=[(0.0, 0.0, 0.0), (0.0, 0.0, 0.97)])
    add_adsorbate(slab, oh, height=1.8, position=site)
    slab.calc = EMT()
    energy = slab.get_potential_energy()
    energies[site] = energy
    write(f"Pt111_OH_{site}.xyz", slab)

for site, energy in energies.items():
    print(f"{site:6s}: {energy:.6f} eV")

best_site = min(energies, key=energies.get)
print(f"Lowest energy site: {best_site} ({energies[best_site]:.6f} eV)")
