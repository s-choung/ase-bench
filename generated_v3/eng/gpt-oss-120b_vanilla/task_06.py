from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# Build 2x2x2 Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# Initialise velocities at 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Report initial state
init_temp = atoms.get_temperature()
init_pot  = atoms.get_potential_energy()
init_kin  = atoms.get_kinetic_energy()
print(f'Initial  T = {init_temp:6.2f} K')
print(f'Initial  Epot = {init_pot:12.4f} eV')
print(f'Initial  Ekin = {init_kin:12.4f} eV')

# Langevin MD: 5 fs timestep, 300 K, friction 0.02 ps⁻¹
dt = 5.0 * units.fs
dyn = Langevin(atoms, dt, temperature_K=300, friction=0.02)

# Run 100 steps
dyn.run(100)

# Report final state
final_temp = atoms.get_temperature()
final_pot  = atoms.get_potential_energy()
final_kin  = atoms.get_kinetic_energy()
print(f'Final    T = {final_temp:6.2f} K')
print(f'Final    Epot = {final_pot:12.4f} eV')
print(f'Final    Ekin = {final_kin:12.4f} eV')
