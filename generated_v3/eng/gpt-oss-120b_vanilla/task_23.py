#!/usr/bin/env python
"""
Pt(111) 3‑layer slab with OH adsorbed on ontop, bridge and fcc hollow sites.
Single‑point EMT energies are computed and the most stable site is reported.
"""

from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT
import copy

# ---- 1. Build the clean Pt(111) slab ---------------------------------
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# ---- 2. Define the OH adsorbate ---------------------------------------
# Simple linear OH, O first (will be the atom that contacts the surface)
bond_length = 0.97          # Å (approx. O–H bond)
OH = molecule('H2O')        # start from H2O, then keep only one H
OH = OH[[0, 2]]              # keep O (0) and one H (2)
OH.positions[1] = [0, 0, bond_length]  # place H above O along z

# ---- 3. Sites to test -------------------------------------------------
sites = {
    'ontop': 'ontop',
    'bridge': 'bridge',
    'fcc_hollow': 'hollow',   # default for fcc(111) is the fcc hollow
}

energies = {}

# ---- 4. Loop over sites, attach OH, compute energy --------------------
for name, site in sites.items():
    surf = copy.deepcopy(slab)
    add_adsorbate(surf, OH, height=1.7, position=site)  # O about 1.7 Å above surface
    surf.center(vacuum=10.0, axis=2)

    surf.calc = EMT()
    energies[name] = surf.get_potential_energy()

# ---- 5. Report results ------------------------------------------------
print("Adsorption energies (eV):")
for name, E in energies.items():
    print(f"  {name:10s}: {E: .6f}")

best_site = min(energies, key=energies.get)
print(f"\nLowest energy site: {best_site} ({energies[best_site]: .6f} eV)")
