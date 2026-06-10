from ase import Atoms
from ase.geometry import get_distances

co2 = Atoms(
    symbols=["C", "O", "O"],
    positions=[(0.0, 0.0, 0.0), (1.16, 0.0, 0.0), (-1.16, 0.0, 0.0)],
    cell=[10.0, 10.0, 10.0],
    pbc=False,
)

_, distances = get_distances(co2.positions, cell=co2.cell, pbc=co2.pbc)

print("Distance matrix (Angstrom):")
print(distances)
print(f"C-O1: {distances[0, 1]:.2f} Å")
print(f"C-O2: {distances[0, 2]:.2f} Å")
print(f"O1-O2: {distances[1, 2]:.2f} Å")
