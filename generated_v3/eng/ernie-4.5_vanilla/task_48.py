from ase.build import bulk
from ase.calculators.emt import EMT
from ase.geometry.geometry import get_distances

# Create a FCC Cu supercell 2x2x2
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True).repeat((2, 2, 2))

# Use EMT calculator (though not strictly necessary for distance calculation)
atoms.calc = EMT()

# Get distances from atom 0 to all other atoms, accounting for PBC
distances = get_distances(atoms.positions, cell=atoms.cell, pbc=atoms.pbc, mic=True)[1][0]

# Print the minimum and maximum distances
print(f"Minimum distance: {distances.min():.2f} Å")
print(f"Maximum distance: {distances.max():.2f} Å")
