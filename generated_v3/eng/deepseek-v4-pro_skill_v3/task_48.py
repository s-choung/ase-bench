from ase.build import bulk
from ase.geometry import get_distances

# Cu FCC 2x2x2 supercell (conventional cell: 4 atoms → 32 atoms)
atoms = bulk('Cu', 'fcc', a=3.61)
atoms *= (2, 2, 2)

# Get distances from atom 0 to all atoms, respecting periodic boundaries
p1 = atoms.positions[0:1]            # shape (1,3)
p2 = atoms.positions                 # shape (natoms,3)
_, D_len = get_distances(p1, p2, cell=atoms.cell, pbc=atoms.pbc)

# Exclude self-distance (zero)
distances = D_len[0]
distances = distances[distances > 1e-12]

print(f"Minimum distance: {distances.min():.4f} Å")
print(f"Maximum distance: {distances.max():.4f} Å")
