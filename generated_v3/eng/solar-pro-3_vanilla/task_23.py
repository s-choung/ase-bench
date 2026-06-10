```python
# ASE imports
from ase import Atoms
from ase.build import fcc111, rectangle
from ase.calculators.emt import EMT

# slab parameters
lat = fcc111("Pt")
lat.cell[2] /= 3  # thickness ~3 atomic layers
lat.center()

# OH molecule
oh = Atoms("OH", positions=[(0, 0, 0), (0, 0, 1.2)],
          cell=lat.cell, pbc=False)

# adsorption sites
sites = []
# ontop
sites.append((oh.translate((0.0, 0.0, 1.55)), "On‑top"))
# bridge
sites.append((oh.translate((-0.12, 0.28, 1.55)), "Bridge"))
# fcc hollow
sites.append((oh.translate((0.16, 0.16, 1.5), atoms=lat), "fcc hollow"))

# calculate and compare
best = None
best_E = 1e10
for adsorb, label in sites:
    adsorb.calc = EMT()
    E = adsorb.get_potential_energy()
    print(f"{label}: {E:.6f} eV")
    if E < best_E:
        best_E = E
        best = label
print(f"\nLowest energy site: {best}")
