from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import bulk
from ase.neighborlist import NeighborList

# Create Cu FCC 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True) * (3, 3, 3)

# Set up EMT calculator
atoms.set_calculator(EMT())

# Create NeighborList using natural cutoffs
nl = NeighborList([1.2 * atoms.get_calculator().get_position_tolerance(), 0.0],
                  self_interaction=False, bothways=True)

nl.update(atoms)

# Get coordination numbers for each atom
coord_nums = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]

# Print average coordination number
print("Average coordination number:", sum(coord_nums) / len(coord_nums))
