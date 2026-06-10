from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# FCC Al 2×2×2 supercell
atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

# Initial volume
V0 = atoms.get_volume()

# Temperature 500 K, pressure 10 GPa → eV/Å³ (1 eV/Å³ = 160.21766208 GPa)
pressure_eV_A3 = 10.0 / 160.21766208

# Initialise velocities & remove COM drift
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# NPT Berendsen MD (1 fs timestep, 100 steps)
dyn = NPTBerendsen(atoms,
                   timestep=1 * units.fs,
                   temperature_K=500,
                   ttime=100 * units.fs,      # thermostat time constant
                   pressure=pressure_eV_A3,
                   pfactor=100 * units.fs)    # barostat time constant
dyn.run(100)

# Final volume
V1 = atoms.get_volume()

print(f'Initial volume: {V0:.3f} Å³')
print(f'Final   volume: {V1:.3f} Å³')
