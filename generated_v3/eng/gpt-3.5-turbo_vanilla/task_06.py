from ase import units
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.langevin import Langevin

# Create FCC Cu bulk 2x2x2 supercell
atoms = FaceCenteredCubic(directions=[[1,0,0],[0,1,0],[0,0,1]], size=(2,2,2), symbol='Cu')

# Set up Langevin dynamics
MaxwellBoltzmannDistribution(atoms, 300*units.kB)
dyn = Langevin(atoms, 5*units.fs, 300*units.kB, 0.002)

# Run dynamics for 100 steps
dyn.run(100)

# Print initial and final temperature and energy
print('Initial T =', dyn.get_temperature(), 'K')
print('Final T   =', dyn.get_temperature(), 'K')
print('Initial E =', atoms.get_potential_energy(), 'eV')
print('Final E   =', atoms.get_potential_energy(), 'eV')
