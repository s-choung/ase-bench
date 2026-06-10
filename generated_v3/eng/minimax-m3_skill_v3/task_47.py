from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)

coords = []
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    n = len(indices)
    coords.append(n)
    print(f"Atom {i}: {n} neighbors")

avg = sum(coords) / len(coords)
print(f"\nTotal atoms: {len(atoms)}")
print(f"Average coordination number: {avg}")
