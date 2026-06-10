import numpy as np
from ase.build import bulk
from ase. neighborlist import natural_cutoff as nc
from ase.calculators.emt import EMT

# build a 3×3×3 Cu FCC supercell
shape = (3, 3, 3)
Cu = bulk('Cu', 'fcc', latticeconstant=3.61, a0=shape, cubic=True)
Cu.set_calculator(EMT())

# create a neighbor list (every pair i < j) with EMT energy cutoff
nl = nc.NaturalCutoffNeighborList(Cu.cell, Cu.pbc, Cu,
                                  nmax=30, skin=0.3, supercell=Cu.get_supercelllist(),
                                  scheme='all',
                                  calculator=Cu.calc)

# number of neighbours for each atom using a skin of 0.3 Å
count = []
for i, atom in enumerate(Cu):
    nbrs = nl.get_neighbors(i)
    count.append(len(nbrs))

avg_cn = np.mean(count)
print(f'Average coordination number (cutoff 0.3 Å): {avg_cn:.2f}')
