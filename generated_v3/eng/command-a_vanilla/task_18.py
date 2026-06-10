from ase.db import connect
from ase.geometry.analysis import Analysis

with connect('https://cmr.fysik.dtu.dk/g2/db.json') as db:
    methan = db.get_atoms('*CH4*')

print('Chemical formula:', methan.get_chemical_formula())
print('Atomic coordinates:')
for atom, pos in zip(methan.get_chemical_symbols(), methan.get_positions()):
    print(f'{atom}: {pos}')

analysis = Analysis(methan)
for i, j in analysis.unique_pairs():
    print(f'Bond length between {methan.symbols[i]} and {methan.symbols[j]}: {analysis.distance(i, j):.4f} Å')
