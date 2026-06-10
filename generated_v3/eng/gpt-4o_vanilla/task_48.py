from ase.build import bulk
from ase.neighborlist import NeighborList

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
nl = NeighborList([3.6/2]*len(atoms), skin=0.3, sorted=False, self_interaction=False)
nl.update(atoms)

indices, distances = atoms.get_distances(0, [i for i in range(1, len(atoms))], mic=True, vector=False)
min_dist, max_dist = distances.min(), distances.max()

print(f'Minimum distance: {min_dist:.3f}')
print(f'Maximum distance: {max_dist:.3f}')
