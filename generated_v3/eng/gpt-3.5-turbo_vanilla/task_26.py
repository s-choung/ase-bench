from ase import Atom, Atoms
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS

# Create FCC Ni bulk
a = 3.52  # Ni lattice constant
bulk = Atoms([Atom('Ni', (0, 0, 0))],
             cell=[(0, a, a), (a, 0, a), (a, a, 0)],
             pbc=True)

# Set up EMT calculator with precon='auto'
bulk.set_calculator(EMT(prec='auto'))

# Optimize using PreconLBFGS until fmax=0.01
opt = PreconLBFGS(bulk, logfile=None)
opt.run(fmax=0.01)

# Print optimization details
print("Number of steps:", opt.get_number_of_steps())
print("Final energy:", bulk.get_potential_energy())
print("Final cell parameters:", bulk.get_cell_lengths_and_angles())
