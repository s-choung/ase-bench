from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# Pd FCC 2×2×2 supercell
atoms = bulk('Pd', 'fcc', a=3.89) * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities at 500 K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# Energy before dynamics
E_start = atoms.get_total_energy() + atoms.get_kinetic_energy()

# NVE MD: Velocity–Verlet, 200 steps, 2 fs timestep
dyn = VelocityVerlet(atoms, dt=2 * units.fs)
dyn.run(200)

# Energy after dynamics
E_end = atoms.get_total_energy() + atoms.get_kinetic_energy()

print(f'Energy difference (eV): {E_end - E_start:.6f}')
