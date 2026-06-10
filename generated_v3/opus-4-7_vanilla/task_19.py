from ase import Atoms

co2 = Atoms('OCO',
            positions=[[-1.16, 0, 0], [0, 0, 0], [1.16, 0, 0]],
            cell=[10, 10, 10],
            pbc=False)

d = co2.get_distances(1, [0, 2])
print("C-O1:", d[0])
print("C-O2:", d[1])
print("O1-O2:", co2.get_distance(0, 2))
