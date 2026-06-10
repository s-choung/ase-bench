from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

# Set initial temperature to 300K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Initial total energy
init_energy = atoms.get_total_energy()

# Set up NVE MD with VelocityVerlet
dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)

# Run 50 steps
dyn.run(50)

# Final total energy
final_energy = atoms.get_total_energy()

print(f"Initial total energy: {init_energy:.6f} eV")
print(f"Final total energy:   {final_energy:.6f} eV")
print(f"Energy difference:    {final_energy - init_energy:.6e} eV")
