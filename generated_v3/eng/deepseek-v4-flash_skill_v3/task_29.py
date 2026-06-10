from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Build Pd FCC 2x2x2 supercell
atoms = bulk('Pd', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

# Set initial velocities at 500 K, remove COM drift
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Run VelocityVerlet NVE MD
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
start_energy = atoms.get_kinetic_energy() + atoms.get_potential_energy()
dyn.run(200)
end_energy = atoms.get_kinetic_energy() + atoms.get_potential_energy()

print(f"Total energy start: {start_energy:.6f} eV")
print(f"Total energy end:   {end_energy:.6f} eV")
print(f"Difference:         {end_energy - start_energy:.6e} eV")
