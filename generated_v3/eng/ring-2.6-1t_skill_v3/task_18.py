from ase.collections import g2
from ase.neighborlist import natural_cutoffs, NeighborList

ch4 = g2['CH4']

print('Atomic coordinates:')
for a in ch4:
    print(f'  {a.symbol:2s} {a.position[0]:10.5f} {a.position[1]:10.5f} {a.position[2]:10.5f}')

print('\nBond lengths:')
cutoffs = natural_cutoffs(ch4, mult=1.1)
nl = NeighborList(cutoffs)
nl.update(ch4)
for i in range(len(ch4)):
    neighs, _ = nl.get_neighbors(i)
    for j in neighs:
        if i < j:
            d = ch4.get_distance(i, j)
            print(f'  {ch4[i].symbol}-{ch4[j].symbol}: {d:.3f} Å')

print(f'\nChemical formula: {ch4.get_chemical_formula()}')
