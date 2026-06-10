from ase.collections import g2
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

# Retrieve methane molecule
atoms = g2["CH4"]

# Print atomic coordinates
print("Atomic coordinates (Å):")
for i, (symbol, pos) in enumerate(zip(atoms.get_chemical_symbols(),
                                      atoms.get_positions())):
    print(f"{i:2d} {symbol:2s} {pos[0]: .6f} {pos[1]: .6f} {pos[2]: .6f}")

# Print chemical formula
print("\nChemical formula:", atoms.get_chemical_formula())

# Determine and print bond lengths
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

print("\nBond lengths (Å):")
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    for j, offset in zip(indices, offsets):
        if i < j:  # avoid double counting
            # Real vector accounting for periodic offsets (none for isolated molecule)
            vec = atoms.positions[i] - (atoms.positions[j] + np.dot(offset, atoms.get_cell()))
            dist = np.linalg.norm(vec)
            print(f"{atoms[i].symbol}-{atoms[j].symbol}: {dist:.3f}")
