from ase import Atoms

co2 = Atoms('OCO',
            positions=[(-1.16, 0, 0), (0, 0, 0), (1.16, 0, 0)],
            cell=[10, 10, 10],
            pbc=False)

print("C-O1 distance:", co2.get_distance(1, 0))
print("C-O2 distance:", co2.get_distance(1, 2))
print("O1-O2 distance:", co2.get_distance(0, 2))
