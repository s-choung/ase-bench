from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.langevin import Langevin

# Cu FCC bulk, 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities for 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300 * units.kB)
Stationary(atoms)  # remove center-of-mass drift

# Initial temperature and potential energy
T_init = atoms.get_temperature()
E_init = atoms.get_potential_energy()
print(f"Initial T = {T_init:.2f} K, E_pot = {E_init:.3f} eV")

# Langevin dynamics (NVT) at 300 K, 5 fs timestep
dyn = Langevin(atoms,
               timestep=5 * units.fs,
               temperature_K=300,
               friction=0.01 / units.fs)
dyn.run(100)

# Final temperature and potential energy
T_final = atoms.get_temperature()
E_final = atoms.get_potential_energy()
print(f"Final   T = {T_final:.2f} K, E_pot = {E_final:.3f} eV")
