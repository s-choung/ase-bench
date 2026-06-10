from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = bulk('Cu', 'fcc', a=3.6).repeat((3, 3, 3))
atoms.calc = EMT()
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)
coords = [len(nl.get_neighbors(i)) for i in range(len(atoms))]
print(sum(coords) / len(coords))
