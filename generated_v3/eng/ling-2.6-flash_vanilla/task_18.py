from ase.db import connect
from ase.geometry import get_distances

with connect('G2.db') as db:
    row = db.get(name='CH4')
    print('Chemical formula:', row.get_chemical_formula())
    print('Atomic coordinates:\n', row.positions)
    dist, _ = get_distances(row.positions, row.positions)
    for i, j in zip(*row.get_all_distances(mic=True, vector=True)):
        print(f'Bond length between {row.symbols[i]} and {row.symbols[j]}: {dist[i,j]:.3f} Å')
