from ase import Atoms
from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)
atoms = atoms.repeat((3, 3, 3))
atoms.set_calculator(EMT())
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

coordination_numbers = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
average = sum(coordination_numbers) / len(coordination_numbers)
print("Average coordination number:", average)
