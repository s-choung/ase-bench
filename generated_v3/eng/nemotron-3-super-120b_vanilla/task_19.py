from ase import Atoms

co2 = Atoms('COO',
            positions=[(0.0, 0.0, 0.0),
                       (0.0, 0.0, 1.16),
                       (0.0, 0.0, -1.16)],
            cell=[10, 10, 10],
            pbc=False)

dist = co2.get_all_distances(mic=False)

n = len(co2)
for i in range(n):
    for j in range(i+1, n):
        print(f"Distance {co2[i].symbol}{i}-{co2[j].symbol}{j}: {dist[i, j]:.3f} Å")
