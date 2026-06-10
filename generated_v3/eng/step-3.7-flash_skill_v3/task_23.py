from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase import Atoms

# Create 3-layer Pt(111) slab with vacuum
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)

# Create OH adsorbate and shift so O atom lies at its center of mass
oh = Atoms('OH', positions=[[0, 0, 0], [0, 0, 0.96]])
com = oh.get_center_of_mass()
oh.translate(com - oh.positions[0])

sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    s = slab.copy()
    add_adsorbate(s, oh, height=2.0, position=site)
    s.calc = EMT()
    energies[site] = s.get_potential_energy()

min_site = min(energies, key=energies.get)
print("Site energies (eV):")
for site, e in energies.items():
    print(f"  {site}: {e:.4f}")
print(f"Lowest energy site: {min_site} ({energies[min_site]:.4f} eV)")
