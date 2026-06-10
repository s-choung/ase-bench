from ase import Atoms
import numpy as np

positions = [[-1.16, 0.0, 0.0], [0.0, 0.0, 0.0], [1.16, 0.0, 0.0]]
co2 = Atoms(symbols=['O', 'C', 'O'], positions=positions, cell=[10, 10, 10], pbc=False)

# Full distance matrix (3x3)
all_d = co2.get_all_distances()
print("All interatomic distances (Å):")
print(np.array2string(all_d, precision=4, suppress_small=True))

# Specific pair distances
print(f"\nO(0)–C(1): {co2.get_distances(0, 1)[0]:.4f} Å")
print(f"C(1)–O(2): {co2.get_distances(1, 2)[0]:.4f} Å")
print(f"O(0)–O(2): {co2.get_distances(0, 2)[0]:.4f} Å")
