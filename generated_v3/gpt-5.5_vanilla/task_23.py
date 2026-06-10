from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

sites = ["ontop", "bridge", "fcc"]
energies = {}

base = fcc111("Pt", size=(3, 3, 3), vacuum=10.0)

for site in sites:
    slab = base.copy()
    oh = Atoms("OH", positions=[(0, 0, 0), (0, 0, 0.97)])
    add_adsorbate(slab, oh, height=2.0, position=site, mol_index=0)
    slab.calc = EMT()
    energies[site] = slab.get_potential_energy()

for site, energy in energies.items():
    print(f"{site}: {energy:.6f} eV")

best = min(energies, key=energies.get)
print(f"lowest: {best} ({energies[best]:.6f} eV)")
