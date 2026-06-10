from ase import Atoms

co2 = Atoms(
    symbols=["C", "O", "O"],
    positions=[(0.0, 0.0, 0.0), (1.16, 0.0, 0.0), (-1.16, 0.0, 0.0)],
    cell=[10.0, 10.0, 10.0],
    pbc=False,
)

for i, j in [(0, 1), (0, 2), (1, 2)]:
    d = co2.get_distances(i, [j])[0]
    print(f"{co2[i].symbol}{i}-{co2[j].symbol}{j}: {d:.3f} Å")
