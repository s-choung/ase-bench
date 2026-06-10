from ase.build import fcc111
from ase.calculators import EMT
from ase.neighborlist import NeighborList
from ase.io import write

calc = EMT(xc='LDA')
cubo = fcc111('Cu', size=(3, 3, 3), a=3.615, shift=(0, 0, 0), calc=calc)
nl = NeighborList(cubo, cutoff=2.0)
nl.build()
coord = cubo.positions
n_neighbors = [len(nl.get_neighbors(i)) for i in range(len(cubo))]
avg_coord = np.mean(n_neighbors)
print(f"Average coordination number: {avg_coord}")
write('cu_coord.xyz', cubo)
