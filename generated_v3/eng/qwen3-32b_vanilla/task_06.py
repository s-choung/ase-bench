from ase import units, bulk, velocities
from ase.calculators.emt import EMT
from ase.dynamics import Langevin

atoms = bulk('Cu').repeat((2, 2, 2))
atoms.calc = EMT()
velocities.MaxwellBoltzmannDistribution(atoms, temperature_K=300)
T_initial = atoms.get_temperature()
E_initial = atoms.get_potential_energy()
dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.02)
dyn.run(100)
T_final = atoms.get_temperature()
E_final = atoms.get_potential_energy()
print(f'Initial Temperature: {T_initial:.2f} K, Energy: {E_initial:.2f} eV')
print(f'Final Temperature: {T_final:.2f} K, Energy: {E_final:.2f} eV')
