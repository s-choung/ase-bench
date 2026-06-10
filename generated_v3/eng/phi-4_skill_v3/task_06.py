from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.velocitydistribution import Stationary
from ase.units import fs, kB

# Create a 2x2x2 supercell of Cu in FCC structure
atoms = bulk('Cu', 'fcc', a=3.615, cubic=True).repeat((2, 2, 2))

# Set EMT calculator
atoms.calc = EMT()

# Set the initial velocities to Maxwell-Boltzmann distribution at 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Remove any initial drift of the center of mass and rotation
Stationary(atoms)

# Set up the Langevin dynamics
md = Langevin(atoms, dt=5*fs, temperature_K=300, friction=0.01/fs)

# Print initial temperature and energy
initial_temp = atoms.get_kinetic_energy() / (1.5 * len(atoms) * kB * 300)
initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f'Initial Temperature: {initial_temp:.2f} K')
print(f'Initial Energy: {initial_energy:.2f} eV')

# Run the simulation for 100 steps
md.run(100)

# Print final temperature and energy
final_temp = atoms.get_kinetic_energy() / (1.5 * len(atoms) * kB * 300)
final_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f'Final Temperature: {final_temp:.2f} K')
print(f'Final Energy: {final_energy:.2f} eV')
