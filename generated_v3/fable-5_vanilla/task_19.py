from ase import Atoms

co2 = Atoms('OCO',
            positions=[(-1.16, 0, 0), (0, 0, 0), (1.16, 0, 0)],
            cell=[10, 10, 10],
            pbc=False)

d_co1 = co2.get_distance(1, 0)
d_co2 = co2.get_distance(1, 2)
d_oo = co2.get_distance(0, 2)

print(f"C-O1 distance: {d_co1:.3f} A")
print(f"C-O2 distance: {d_co2:.3f} A")
print(f"O-O distance:  {d_oo:.3f} A")

print(co2.get_distances(1, [0, 2]))
