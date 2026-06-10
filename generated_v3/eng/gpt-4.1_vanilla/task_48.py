from ase.build import bulk
from ase.calculators.emt import EMT

# Build 2x2x2 Cu FCC supercell
atoms = bulk("Cu", "fcc", a=3.6).repeat((2,2,2))
atoms.calc = EMT()

# Get distances from atom 0 to all others, account for PBC
dists = atoms.get_distances(0, range(len(atoms)), mic=True)

# Exclude self-distance (should be zero)
dists = dists[dists > 1e-5]

print(f"Minimum distance: {dists.min():.4f} Å")
print(f"Maximum distance: {dists.max():.4f} Å")
