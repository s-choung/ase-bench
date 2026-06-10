from ase.build import bulk
from ase.calculators.emt import EMT
from ase.geometry import get_distances

# Create a 2x2x2 Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

# Get distances from atom 0 to all other atoms (1 to N-1)
# mic=True accounts for periodic boundary conditions
distances = get_distances(atoms, 0, range(1, len(atoms)), mic=True)

print(f"Minimum distance: {min(distances):.4f} Å")
print(f"Maximum distance: {max(distances):.4f} Å")
