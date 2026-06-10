from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Build 2x2x2 FCC Pd supercell
atoms = bulk('Pd', 'fcc').repeat((2, 2, 2))
atoms.calc = EMT()

# Initialize velocities to 500K, remove center-of-mass drift
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Calculate initial total energy
e_initial = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# Run NVE VelocityVerlet MD for 200 steps, 2fs timestep
dyn = VelocityVerlet(atoms, timestep=2*units.fs)
dyn.run(steps=200)

# Calculate final total energy and print difference
e_final = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Total energy difference (start vs end, eV): {e_final - e_initial:.6f}")
