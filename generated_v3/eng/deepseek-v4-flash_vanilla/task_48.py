from ase.build import bulk
from ase.neighborlist import neighbor_list

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)

distances = neighbor_list('d', atoms, {('Cu', 'Cu'): 10.0}, self_interaction=False,
                         max_nth=len(atoms), mic=True, bothways=False, 
                         include_partials=False)[0]

i = 0
dists = []
for j in range(1, len(atoms)):
    d = atoms.get_distance(i, j, mic=True)
    dists.append(d)

print(f"Minimum distance: {min(dists):.3f} Å")
print(f"Maximum distance: {max(dists):.3f} Å")
