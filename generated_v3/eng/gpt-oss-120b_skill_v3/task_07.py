from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Initial velocities (300 K) and remove centre‑of‑mass drift
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

def total_energy(at):
    return at.get_potential_energy() + at.get_kinetic_energy()

print(f'Initial total energy: {total_energy(atoms):.6f} eV')

# NVE MD (VelocityVerlet) for 50 steps
dyn = VelocityVerlet(atoms, timestep=1 * units.fs)
for _ in range(50):
    dyn.run(1)

print(f'Final total energy:   {total_energy(atoms):.6f} eV')
