from ase.collections import g2

atoms = g2['CH4']
print("Coordinates:\n", atoms.positions)
print("Bond lengths (Å):", atoms.get_distances(0, [1, 2, 3, 4]))
print("Chemical formula:", atoms.symbols)
