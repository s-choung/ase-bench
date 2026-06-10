from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.nptberendsen import NPTBerendsen
from ase import units

# Cu FCC 3x3x3 supercell
cu = bulk('Cu', 'fcc', a=3.615) * (3, 3, 3)
cu.calc = EMT()

# Initialize velocities at 300 K
MaxwellBoltzmannDistribution(cu, temperature_K=300)

# Initial state
vol0 = cu.get_volume()
p0 = cu.get_pressure() * units.GPa * 10000  # convert to bar
print(f'Initial volume: {vol0:.3f} Å^3, pressure: {p0:.1f} bar')

# NPT Berendsen dynamics
dyn = NPTBerendsen(cu,
                   timestep=5 * units.fs,
                   temperature_K=300,
                   taut=100 * units.fs,
                   taup=1000 * units.fs,
                   pressure=1.0 * units.bar)
dyn.run(200)

# Final state
vol1 = cu.get_volume()
p1 = cu.get_pressure() * units.GPa * 10000
print(f'Final volume: {vol1:.3f} Å^3, pressure: {p1:.1f} bar')
