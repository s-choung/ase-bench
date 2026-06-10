from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS

# Set up the Ni FCC bulk
ni = bulk('Ni', 'fcc', a=3.52)

# Attach EMT calculator
ni.calc = EMT()

# Optimize using PreconLBFGS
opt = PreconLBFGS(ni, precon='auto')
opt.run(fmax=0.01)

# Output
print('Number of steps:', len(opt.get_traj()))
print('Final energy:', ni.get_potential_energy())
print('Cell parameters:', ni.cell)
