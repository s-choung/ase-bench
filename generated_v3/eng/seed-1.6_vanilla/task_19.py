from ase.atoms import Atoms

co2 = Atoms('COO',
            positions=[[0.0, 0.0, 0.0], [1.16, 0.0, 0.0], [-1.16, 0.0, 0.0]],
            cell=[10, 10, 10],
            pbc=False)

c_o_dists = co2.get_distances(0, [1, 2])
o_o_dist = co2.get_distances(1, [2])[0]

print(f'C-O distances: {c_o_dists} Å')
print(f'O-O distance: {o_o_dist} Å')
