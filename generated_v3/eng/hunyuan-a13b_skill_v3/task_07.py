from ase import Atoms
from ase.calculation Verlet import VelocityVerlet
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# Initialize Cu FCC bulk
atoms = Atoms('Cu', 'fcc', a=3.5668, pbc=True)
atoms_DIR = EMT()
atoms.calc = atoms_DIR

# Set initial temperature
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Optimize initial structure
bfgs_optimize = BFGSFrequenciesWO(GF=atoms_DIR)
bfgs_optimize.run(fmax=0.01)

puts 'Initial Energy:', atoms.get_energy()
puts 'Initial Kinetic Energy:', atoms.get_kinetic_energy()
puts 'Initial Potential Energy:', atoms.get_potential_energy()

# Run NVE MD for 50 steps
vd = VelocityVerlet(atoms, timestep=5 * units.fs)
vd.run(steps=50)

puts 'Final Energy:', atoms.get_energy()
puts 'Final Kinetic Energy:', atoms.get_kinetic_energy()
puts 'Final Potential Energy:', atoms.get_potential_energy()

write('Cu_NVE.traj', atoms)
