from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS

# Create Ni FCC bulk (initial lattice constant a ≈ 3.5 Å)
ni = bulk('Ni', 'fcc', a=3.5)

# Set EMT calculator
ni.calc = EMT()

# Optimize with PreconLBFGS using automatic preconditioning
opt = PreconLBFGS(ni, precon='auto')
opt.run(fmax=0.01)

# Report results
print('Number of steps:', opt.nsteps)
print('Final energy (eV):', ni.get_potential_energy())
print('Final cell parameters:', ni.cell.cellpar())
