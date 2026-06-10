from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.verlet import VelocityVerlet

# Pd FCC bulk, make 2x2x2 supercell
atoms = bulk('Pd', 'fcc', a=3.89, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

# Initial velocity distribution at 500 K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)  # remove COM drift

# Energy at start
E_start = atoms.get_kinetic_energy() + atoms.get_potential_energy()

# VelocityVerlet NVE MD (2 fs timestep, 200 steps)
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

# Energy at end
E_end = atoms.get_kinetic_energy() + atoms.get_potential_energy()

print(f'Energy difference (end - start): {E_end - E_start:.6f} eV')
