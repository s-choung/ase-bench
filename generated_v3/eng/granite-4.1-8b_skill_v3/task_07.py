from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units

# Create Cu FCC bulk structure
atoms = bulk('Cu', 'fcc', a=3.615)

# Set calculator
atoms.calc = EMT()

# Relax the structure to get a stable geometry
opt = BFGS(atoms)
opt.run(fmax=0.0001)

# Set initial temperature to 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Perform NVE MD using Velocity Verlet
md = VelocityVerlet(atoms, timestep=5 * units.fs)

# Initial total energy (kinetic + potential)
E_initial = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Initial total energy: {E_initial:.6f} eV")

# Run MD for 50 steps
md.run(nsteps=50)

# Final total energy (kinetic + potential)
E_final = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Final total energy: {E_final:.6f} eV")
