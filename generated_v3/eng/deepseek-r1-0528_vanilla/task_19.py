from ase import Atoms

co2 = Atoms('CO2', positions=[(0, 0, 0), (1.16, 0, 0), (-1.16, 0, 0)])
co2.cell = [10, 10, 10]
co2.pbc = False

distances = co2.get_distances(mic=False)
print(distances)
