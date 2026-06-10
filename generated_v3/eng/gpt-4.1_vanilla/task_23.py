from ase.build import fcc111, add_adsorbate
from ase import Atoms
from ase.calculators.emt import EMT

# Pt(111) slab
slab = fcc111('Pt', size=(2,2,3), vacuum=10.0, periodic=True)

# OH adsorbate
oh = Atoms('OH', positions=[(0, 0, 0), (0, 0, 0.97)])

# Adsorption sites: ontop, bridge, fcc
sites = {
    'ontop': slab[0].position[:2],
    'bridge': 0.5*(slab[0].position[:2] + slab[1].position[:2]),
    'fcc': (
        slab[0].position[:2] +
        slab[1].position[:2] +
        slab[2].position[:2]
    ) / 3
}

energies = {}
for site, (x, y) in sites.items():
    struct = slab.copy()
    add_adsorbate(struct, oh, height=1.1, position=(x, y))
    struct.calc = EMT()
    energies[site] = struct.get_potential_energy()

min_site = min(energies, key=energies.get)

for site, e in energies.items():
    print(f"{site}: {e:.3f} eV")
print(f"Lowest energy site: {min_site}")
