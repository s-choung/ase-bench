from ase import Atoms
from ase.geometry import get_distances

# Create CO2 molecule
symbols = ['C', 'O', 'O']
positions = [[0.0, 0.0, 0.0],   # C at origin
             [1.16, 0.0, 0.0],  # O1 at +x
             [-1.16, 0.0, 0.0]] # O2 at -x
atoms = Atoms(symbols=symbols, positions=positions)
atoms.cell = [10.0, 10.0, 10.0]
atoms.pbc = False

# Calculate interatomic distances
distances = get_distances(atoms, indices=[(0,1), (0,2), (1,2)])
print(f"C-O distance: {distances[0][0]:.2f} Å")
print(f"C-O distance: {distances[0][1]:.2f} Å")
print(f"O-O distance: {distances[0][2]:.2f} Å")
