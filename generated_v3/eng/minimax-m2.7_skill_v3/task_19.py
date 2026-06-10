from ase import Atoms
from ase.geometry import get_distances

co2 = Atoms('OCO', positions=[(0, 0, 0), (-1.16, 0, 0), (1.16, 0, 0)])
co2.set_cell([10, 10, 10])
co2.set_pbc(False)

distances = get_distances(co2)
print(f"Distance matrix (Å):\n{distances}")
print(f"\nC-O bond lengths: {distances[0,1]:.2f} Å, {distances[0,2]:.2f} Å")
print(f"O-O distance: {distances[1,2]:.2f} Å")
