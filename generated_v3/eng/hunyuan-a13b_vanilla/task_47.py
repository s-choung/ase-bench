from ase import Atoms, NeighborList
from ase.calculators import EMT

# Cu FCC structure
fcc_cell = [[0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]]
coords = fcc_cell * 3  # 3x3x3 supercell
Cu = Atoms('Cu', positions=coords, cell=fcc_cell, pbc=True)

# EMT calculator (not used directly for NeighborList)
calc = EMT()

# NeighborList with natural cutoffs
nl = NeighborList(Cu, maximize_cells=True, natural_cutoff=1.2)

# Get neighbor indices
neighbor_indices = [nl.get_neighbors(i) for i in range(len(Cu))]

# Calculate coordination numbers
coord_numbers = [len(neighbors) for neighbors in neighbor_indices]

# Print results
print(f"Coordination numbers: {coord_numbers}")
print(f"Average coordination number: {sum(coord_numbers) / len(coord_numbers)}")
