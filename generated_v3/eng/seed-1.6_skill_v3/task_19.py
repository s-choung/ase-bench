from ase import Atoms
from ase.geometry import get_distances

# Manual CO2 construction
co2 = Atoms(
    symbols=['C', 'O', 'O'],
    positions=[(0.0, 0.0, 0.0), (1.16, 0.0, 0.0), (-1.16, 0.0, 0.0)],
    cell=(10, 10, 10),
    pbc=False
)

# Calculate interatomic distances
d_c_o1 = get_distances([0], [1], co2.cell, co2.pbc)[0][0][0]
d_c_o2 = get_distances([0], [2], co2.cell, co2.pbc)[0][0][0]
d_o_o = get_distances([1], [2], co2.cell, co2.pbc)[0][0][0]

# Print results
print(f'C-O1: {d_c_o1:.2f} Å')
print(f'C-O2: {d_c_o2:.2f} Å')
print(f'O-O: {d_o_o:.2f} Å')
