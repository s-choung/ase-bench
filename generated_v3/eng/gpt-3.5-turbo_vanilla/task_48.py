from ase.build import bulk
from ase.calculators.emt import EMT
from ase.neighborlist import NeighborList

# Create a Cu FCC bulk 2x2x2 supercell
atoms = bulk('Cu', cubic=True, a=3.61, orthorhombic=True)

# Set up the EMT calculator
atoms.set_calculator(EMT())

# Calculate the distances between atom 0 and all other atoms
nl = NeighborList(cutoffs=[2.0 / 3.61], self_interaction=False, bothways=True, skin=0.1)
nl.update(atoms)
distances = nl.get_distances(0, range(1, len(atoms)), mic=True)

# Print the minimum and maximum distances
print(f"Minimum distance: {min(distances)}")
print(f"Maximum distance: {max(distances)}")
