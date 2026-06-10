from ase.data.molecules import molecule
from ase.calculators.emt import EMT
from ase.geometry import get_distances
import numpy as np

# retrieve CH4 from the ASE G2 test set
atoms = molecule('CH4')
atoms.calc = EMT()                     # attach a built‑in calculator (not used here)

# atomic coordinates
print("Atomic coordinates (Å)")
for atom in atoms:
    print(f"{atom.symbol:2s}  {atom.position}")

# chemical formula
print("\nChemical formula:", atoms.get_chemical_formula())

# C–H bond lengths (first atom is carbon)
c_pos = atoms.positions[0]
h_pos = atoms.positions[1:]
_, dists = get_distances(c_pos, h_pos, mic=False)

print("\nBond lengths")
for i, d in enumerate(dists):
    print(f"C–H{i+1}: {d:.3f} Å")
