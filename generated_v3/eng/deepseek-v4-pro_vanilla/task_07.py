from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
import numpy as np

# Create Cu FCC bulk (2x2x2 supercell, 32 atoms)
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

# Set initial velocities at T=300 K and zero total momentum
temp = 300 * units.kB
MaxwellBoltzmannDistribution(atoms, temp)
momenta = atoms.get_momenta()
atoms.set_momenta(momenta - np.sum(momenta, axis=0) / len(atoms))

# Compute initial total energy
pe_initial = atoms.get_potential_energy()
ke_initial = atoms.get_kinetic_energy()
etot_initial = pe_initial + ke_initial
print(f"Initial total energy: {etot_initial:.3f} eV")

# NVE dynamics with Velocity Verlet, 1 fs timestep
dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
dyn.run(50)

# Compute final total energy
pe_final = atoms.get_potential_energy()
ke_final = atoms.get_kinetic_energy()
etot_final = pe_final + ke_final
print(f"Final total energy:   {etot_final:.3f} eV")
