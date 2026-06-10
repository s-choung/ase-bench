from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

# Initial velocities (500 K) and remove COM drift
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Pressure: 10 GPa → eV/Å³  (1 GPa = 0.006241509 eV/Å³)
pressure_GPa = 10.0
pressure = pressure_GPa * 0.006241509   # eV/Å³

# Compressibility ≈ 1/bulk modulus; bulk modulus of Al ≈ 76 GPa
B_GPa = 76.0
compressibility = 1.0 / (B_GPa * 0.006241509)   # Å³/eV

# NPT Berendsen dynamics
dyn = NPTBerendsen(
    atoms,
    timestep=1 * units.fs,
    temperature_K=500,
    pressure=pressure,
    compressibility=compressibility,
)

print(f'Initial volume: {atoms.get_volume():.3f} Å³')
dyn.run(100)
print(f'Final volume:   {atoms.get_volume():.3f} Å³')
