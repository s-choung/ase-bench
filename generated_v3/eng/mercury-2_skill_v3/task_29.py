from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Pd FCC 2x2x2 supercell
atoms = bulk('Pd', 'fcc', a=3.89) * (2, 2, 2)
atoms.calc = EMT()

# Initialise velocities at 500 K and remove COM drift
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Energy before MD
E_start = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# NVE MD for 200 steps, 2 fs timestep
md = VelocityVerlet(atoms, timestep=2 * units.fs)
md.run(200)

# Energy after MD
E_end = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f'Energy change (ΔE): {E_end - E_start:.6f} eV')
