from ase.build import fcc
from ase.calculators.emt import EMT
from ase.neighborlist import NeighborList

atoms = fcc('Cu', size=(3, 3, 3))
calc = EMT()
atoms.calc = calc

nl = NeighborList(atoms, cutoff=atoms.get_cutoffs(calc))
nl.update()

neighbor_counts = [len(n) for n in nl.neighbor_list]
avg_coord = sum(neighbor_counts) / len(atoms)

print(avg_coord)
