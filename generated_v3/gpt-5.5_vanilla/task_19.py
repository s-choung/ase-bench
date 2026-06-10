from ase import Atoms

co2 = Atoms(
    symbols=["O", "C", "O"],
    positions=[[-1.16, 0.0, 0.0], [0.0, 0.0, 0.0], [1.16, 0.0, 0.0]],
    cell=[10.0, 10.0, 10.0],
    pbc=False,
)

print("C-O distances:", co2.get_distances(1, [0, 2]))
print("O-O distance:", co2.get_distances(0, [2]))
