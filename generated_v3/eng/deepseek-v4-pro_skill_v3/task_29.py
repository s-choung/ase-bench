from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Setup Pd FCC 2x2x2 supercell
atoms = bulk('Pd', 'fcc', a=3.89) * (2, 2, 2)
atoms.calc = EMT()

# Initial velocities at 500 K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

initial_total = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# Run NVE MD for 200 steps, 2 fs timestep
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

final_total = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Total energy change (eV): {final_total - initial_total:.6f}")
