from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Build initial structure: Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

# Record initial volume
vol_initial = atoms.get_volume()

# Set initial velocities at 500 K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Define NPT dynamics (10 GPa ≈ 10 * units.GPa eV/Å³)
pressure = 10 * units.GPa
dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=500,
    taut=0.5 * 1000 * units.fs,
    pressure_au=pressure,
    taup=0.5 * 1000 * units.fs,
)

# Run 100 steps
dyn.run(100)

# Record final volume
vol_final = atoms.get_volume()

print(f"Initial volume: {vol_initial:.3f} Å³")
print(f"Final volume: {vol_final:.3f} Å³")
