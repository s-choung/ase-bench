from ase.build import bulk
from ase.neighborlist import NeighborList
from ase import Atoms
from ase.geometry import get_distances
import numpy as np

atoms = bulk('Cu', 'fcc', a=4.0)
atoms.set_cell((4, 4, 4), scale_atoms=True)
nl = NeighborList(atoms, cutoff=5.0, mic=True)

distances = get_distances(atoms[0], atoms, nl)

min_distance = np.min(distances)
max_distance = np.max(distances)

print(f"Minimum distance: {min_distance:.3f} Å")
print(f"Maximum distance: {max_distance:.3f} Å")
