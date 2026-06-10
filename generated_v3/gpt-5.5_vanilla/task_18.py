from ase.collections import g2
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = g2["CH4"]

print("Chemical formula:", atoms.get_chemical_formula())

print("\nAtomic coordinates (Angstrom):")
for i, atom in enumerate(atoms):
    x, y, z = atom.position
    print(f"{i:2d} {atom.symbol:2s} {x:12.6f} {y:12.6f} {z:12.6f}")

cutoffs = natural_cutoffs(atoms, mult=1.2)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

print("\nBond lengths (Angstrom):")
seen = set()
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    for j, offset in zip(indices, offsets):
        pair = tuple(sorted((i, j)))
        if pair in seen:
            continue
        seen.add(pair)
        d = atoms.get_distance(i, j, mic=False)
        print(f"{i:2d}-{j:2d} {atoms[i].symbol}-{atoms[j].symbol}: {d:.6f}")
