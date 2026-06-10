from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.units import kB

# Create Cu FCC bulk
atoms = Atoms('Cu', positions=[(0, 0, 0)], cell=[[2.55, 2.55, 0], [2.55, 0, 2.55], [0, 2.55, 2.55]], pbc=True)
atoms.set_calculator(EMT())

# Set initial temperature to 300K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Print initial total energy
print(f"Initial total energy: {atoms.get_potential_energy() + atoms.get_kinetic_energy():.6f} eV")

# Run NVE MD
dyn = VelocityVerlet(atoms, 1.0 * atoms.get_masses()[0] / kB)
dyn.run(50)

# Print final total energy
print(f"Final total energy: {atoms.get_potential_energy() + atoms.get_kinetic_energy():.6f} eV")
