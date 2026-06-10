from ase import Atoms
from ase.build import fcc111, molecule
from ase.calculators.emt import EMT

# Pt(111) slab, 3 layers, 2x2 supercell, 10 Å vacuum
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# OH adsorbate (approximate geometry)
oh = Atoms('OH', positions=[[0, 0, 0], [0, 0, 0.97]])

sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    slab_copy = slab.copy()
    add_adsorbate(slab_copy, oh, height=1.8, position=site)
    slab_copy.calc = EMT()
    energies[site] = slab_copy.get_potential_energy()
    print(f"{site}: {energies[site]:.3f} eV")

best_site = min(energies, key=energies.get)
print(f"\nLowest energy site: {best_site} ({energies[best_site]:.3f} eV)")
