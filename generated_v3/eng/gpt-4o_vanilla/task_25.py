from ase.build import bulk
from ase.constraints import ExpCellFilter
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create copper FCC bulk
cu_bulk = bulk('Cu', 'fcc', a=3.6)

# Set calculator
cu_bulk.set_calculator(EMT())

# Print initial cell and energy
print("Initial cell:", cu_bulk.cell)
print("Initial energy:", cu_bulk.get_potential_energy())

# Set up cell filter for simultaneous lattice and atomic position optimization
ecf = ExpCellFilter(cu_bulk)

# Optimize with BFGS
optimizer = BFGS(ecf)
optimizer.run(fmax=0.01)

# Print final cell and energy
print("Optimized cell:", cu_bulk.cell)
print("Final energy:", cu_bulk.get_potential_energy())
