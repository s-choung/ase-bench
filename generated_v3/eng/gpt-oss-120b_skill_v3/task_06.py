from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Build 2×2×2 Cu fcc supercell
atoms = bulk('Cu', 'fcc') * (2, 2, 2)
atoms.calc = EMT()

# Initial state (300 K)
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Record initial temperature and energies
temp_i = atoms.get_temperature()
pot_i = atoms.get_potential_energy()
kin_i = atoms.get_kinetic_energy()
tot_i = pot_i + kin_i
print(f'Initial  T = {temp_i:.1f} K,  Epot = {pot_i:.4f} eV,  Ekin = {kin_i:.4f} eV,  Etot = {tot_i:.4f} eV')

# Langevin dynamics (NVT, 5 fs timestep, 100 steps)
dyn = Langevin(atoms,
               timestep=5 * units.fs,
               temperature_K=300,
               friction=0.01 / units.fs)
dyn.run(100)

# Final temperature and energies
temp_f = atoms.get_temperature()
pot_f = atoms.get_potential_energy()
kin_f = atoms.get_kinetic_energy()
tot_f = pot_f + kin_f
print(f'Final    T = {temp_f:.1f} K,  Epot = {pot_f:.4f} eV,  Ekin = {kin_f:.4f} eV,  Etot = {tot_f:.4f} eV')
