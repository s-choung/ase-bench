from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

# Set initial velocities at 500 K
temp_K = 500
MaxwellBoltzmannDistribution(atoms, temp=temp_K * units.kB)

# Convert pressure: 10 GPa → eV/Å³
pressure = 10 * units.GPa
print(f'Pressure: {pressure} eV/Å³')

# Initial volume
vol_initial = atoms.get_volume()
print(f'Initial cell volume: {vol_initial:.3f} Å³')

# NPT Berendsen dynamics
md = NPTBerendsen(atoms,
                  timestep=1 * units.fs,
                  temperature=temp_K * units.kB,
                  pressure=pressure,
                  taut=100 * units.fs,
                  taup=1000 * units.fs)

for _ in range(100):
    md.step()

# Final volume
vol_final = atoms.get_volume()
print(f'Final cell volume: {vol_final:.3f} Å³')
