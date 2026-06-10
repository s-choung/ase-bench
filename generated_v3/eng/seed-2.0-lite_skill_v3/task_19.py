from ase import Atoms
from ase.geometry import get_distances

# Manually build CO2 molecule
co2 = Atoms(
    symbols=['C', 'O', 'O'],
    positions=[[0.0, 0.0, 0.0],  # C at origin
               [1.16, 0.0, 0.0],  # First O 1.16 Å along +x
               [-1.16, 0.0, 0.0]], # Second O 1.16 Å along -x
    cell=[10.0, 10.0, 10.0],  # 10x10x10 Å cubic box
    pbc=False
)

# Calculate and print interatomic distances
distance_matrix, _ = get_distances(co2.get_positions(), cell=co2.get_cell(), pbc=co2.get_pbc())
print("Interatomic distance matrix (Å):\n", distance_matrix.round(3))
