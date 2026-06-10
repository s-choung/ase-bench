from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

sites = {
    "ontop": ("ontop", 1.8),
    "bridge": ("bridge", 1.8),
    "fcc": ("fcc", 1.8),
}

results = {}

for name, (site, height) in sites.items():
    slab = fcc111("Pt", size=(2, 2, 3), vacuum=10.0)
    oh = molecule("OH")
    add_adsorbate(slab, oh, height=height, position=site)
    slab.calc = EMT()
    e = slab.get_potential_energy()
    results[name] = e
    print(f"{name}: {e:.6f} eV")

best = min(results, key=results.get)
print(f"Lowest energy site: {best} ({results[best]:.6f} eV)")
