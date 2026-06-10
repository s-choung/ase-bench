from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Build Cu FCC 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.61) * (3, 3, 3)
atoms.calc = EMT()

# Initial state
print(f'Initial volume: {atoms.get_volume():.3f} Å^3')
print(f'Initial pressure: {atoms.get_pressure():.3f} eV/Å^3')

# Initialize velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# NPT Berendsen dynamics
dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure_au=1.0 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs,
)
dyn.run(200)

# Final state
print(f'Final volume: {atoms.get_volume():.3f} Å^3')
print(f'Final pressure: {atoms.get_pressure():.3f} eV/Å^3')
