import ase
from ase.lattice.cubic import FaceCenteredCubic
from ase.calculators.emt import EMT
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = FaceCenteredCubic('Cu', a=3.615, size=(3,3,3))
atoms.set_calculator(EMT())
cutoff = natural_cutoffs(atoms)
nl = NeighborList(cutoff, skin=0.1)
nl.update(atoms)
neighbors = nl.get_neighbors(atoms)
avg = sum(len(n) for n in neighbors) / len(atoms)
print(f"Average coordination number: {avg}")
