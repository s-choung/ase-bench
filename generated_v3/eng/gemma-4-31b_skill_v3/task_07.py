from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Setup system
atoms = bulk('Cu', 'fcc', a=3.61)
atoms.calc = EMT()

# Initial conditions
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Energy check function
def get_total_energy(atoms):
    return atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Initial Total Energy: {get_total_energy(atoms):.4f} eV")

# NVE MD
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(50)

print(f"Final Total Energy: {get_total_energy(atoms):.4f} eV")
