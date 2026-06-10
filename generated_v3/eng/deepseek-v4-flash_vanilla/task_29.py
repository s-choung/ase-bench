from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# Create Pd FCC 2x2x2 supercell
atoms = bulk('Pd', 'fcc', a=3.89) * (2, 2, 2)

# Attach EMT calculator
atoms.calc = EMT()

# Set initial velocities for 500 K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# Compute initial total energy (kinetic + potential)
E_kin0 = atoms.get_kinetic_energy()
E_pot0 = atoms.get_potential_energy()
E_total0 = E_kin0 + E_pot0

# Set up VelocityVerlet integrator, timestep 2 fs
integrator = VelocityVerlet(atoms, timestep=2 * units.fs)

# Run 200 steps
integrator.run(200)

# Compute final total energy
E_kin1 = atoms.get_kinetic_energy()
E_pot1 = atoms.get_potential_energy()
E_total1 = E_kin1 + E_pot1

# Print energy difference
print("Total energy difference (end - start): {:.6f} eV".format(E_total1 - E_total0))
