from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.build import bulk

# Create Ni FCC bulk structure
ni = bulk('Ni', 'fcc', a=3.52)

# Set EMT calculator with precon='auto'
ni.calc = EMT()

# Optimize using PreconLBFGS
opt = PreconLBFGS(ni, precon='auto', logfile=None)
opt.run(fmax=0.01)

# Output results
print(f"Steps: {opt.nsteps}")
print(f"Final energy: {ni.get_potential_energy():.4f}")
print(f"Cell parameters: {ni.cell.lengths()}")
