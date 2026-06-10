from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

slab_base = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
bottom_indices = [a.index for a in slab_base if a.tag == 3]

sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    slab = slab_base.copy()
    oh = molecule('OH')
    add_adsorbate(slab, oh, height=2.0, position=site)
    slab.set_constraint(FixAtoms(indices=bottom_indices))
    slab.calc = EMT()
    e = slab.get_potential_energy()
    energies[site] = e
    print(f"Site: {site:10s}  Energy: {e:.4f} eV")

best_site = min(energies, key=energies.get)
print()
print("--- Energy Comparison ---")
for site, e in energies.items():
    marker = " <-- lowest" if site == best_site else ""
    print(f"  {site:10s}: {e:.4f} eV{marker}")
print(f"\nMost stable adsorption site: {best_site}")
