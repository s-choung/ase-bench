from ase import Atoms
from ase.geometry import get_distances

co2 = Atoms('CO2', positions=[[0, 0, 0], [1.16, 0, 0], [-1.16, 0, 0]])
co2.cell = [10, 10, 10]
co2.pbc = False

_, distances, _ = get_distances(co2.positions)
print(f"C-O distances: {distances[0][1]:.2f} Å, {distances[0][2]:.2f} Å")
print(f"O-O distance: {distances[1][2]:.2f} Å")
