from ase import Atoms
from ase.neighborlist import NeighborList
from ase.units import Bohr

# Create CO2 molecule
c_position = (0.0, 0.0, 0.0)  # Carbon at origin
o1_position = (0.0, 0.0, 1.16 / Bohr)  # Oxygen 1 along z-axis
o2_position = (0.0, 0.0, -1.16 / Bohr)  # Oxygen 2 along negative z-axis

# Initialize atoms object
co2 = Atoms('CO2', positions=[c_position, o1_position, o2_position])

# Set periodic boundary conditions to False
co2.set_pbc([False, False, False])

# Use the neighbor list to calculate distances
nl = NeighborList([1.5] * len(co2), bothways=True, self_interaction=False)
nl.update(co2)

# Obtain the distances between atoms
indices, distances = nl.get_neighbors()

# Print interatomic distances
print("Interatomic Distances in CO2 Molecule:")
for idx, dist in zip(indices, distances):
    for neighbor_index, distance in zip(idx, dist):
        atom1 = co2[neighbor_index]
        atom2 = co2[neighbor_index+1]
        print(f"Distance between {atom1.symbol} and {atom2.symbol}: {distance * Bohr:.2f} Å")
