from ase.build import bulk
from ase.calculators.emt import EMT

# Create 2x2x2 Cu FCC supercell, attach built-in EMT calculator
atoms = bulk('Cu', 'fcc').repeat((2, 2, 2))
atoms.calc = EMT()

# Calculate PBC-corrected distances from atom 0 to all other atoms
distances = atoms.get_distances(0, range(1, len(atoms)), mic=True)

# Output min and max distances
min_dist, max_dist = min(distances), max(distances)
print(f"Minimum distance: {min_dist:.3f} Å")
print(f"Maximum distance: {max_dist:.3f} Å")
