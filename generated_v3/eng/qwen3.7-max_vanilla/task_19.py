from ase import Atoms

co2 = Atoms('CO2',
            positions=[[0.0, 0.0, 0.0], [1.16, 0.0, 0.0], [-1.16, 0.0, 0.0]],
            cell=[10.0, 10.0, 10.0],
            pbc=False)

print("Distance matrix (get_all_distances):")
print(co2.get_all_distances())

print("\nDistances from C to O atoms (get_distances):")
print(co2.get_distances(0, [1, 2]))
