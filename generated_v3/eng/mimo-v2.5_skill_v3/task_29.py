from ase.build import bulk, make_supercell
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import (MaxwellBoltzmannDistribution,
                                         Stationary)
from ase import units

# Create Pd FCC supercell (2x2x2)
atoms = bulk('Pd', 'fcc', a=3.92, cubic=True)
atoms = make_supercell(atoms, [[2, 0, 0], [0, 2, 0], [0, 0, 2]])

# Set calculator
atoms.calc = EMT()

# Initialize velocities at 500K and remove COM motion
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Record initial total energy
initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# Run NVE MD for 200 steps with 2 fs timestep
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(steps=200)

# Record final total energy
final_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# Print energy difference
print(f"Initial total energy: {initial_energy:.6f} eV")
print(f"Final total energy:   {final_energy:.6f} eV")
print(f"Energy difference:    {final_energy - initial_energy:.6e} eV")
