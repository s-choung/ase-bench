from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units
from ase.build import bulk

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Set initial temperature to 300K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Print initial total energy
initial_energy = atoms.get_total_energy()
print(f"Initial total energy: {initial_energy:.6f} eV")

# Run NVE MD with VelocityVerlet for 50 steps
dyn = VelocityVerlet(atoms, timestep=5*units.fs)
dyn.run(50)

# Print final total energy
final_energy = atoms.get_total_energy()
print(f"Final total energy: {final_energy:.6f} eV")
print(f"Energy change: {final_energy - initial_energy:.6e} eV")
