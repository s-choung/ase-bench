from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# Create Cu FCC bulk and supercell
atoms = bulk('Cu', 'fcc', a=3.615) * (3, 3, 3)
atoms.set_calculator(EMT())

# Set initial velocities for 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Initial total energy (kinetic + potential)
E_initial = atoms.get_total_energy()
print('Initial total energy (eV):', E_initial)

# NVE MD with VelocityVerlet (50 steps, dt = 1 fs)
dyn = VelocityVerlet(atoms, dt=1.0)
dyn.run(50)

# Final total energy
E_final = atoms.get_total_energy()
print('Final total energy (eV):', E_final)
