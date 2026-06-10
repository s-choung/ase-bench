from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Build 2x2x2 Al FCC supercell
atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

# Record initial volume
print(f"Initial volume: {atoms.get_volume():.4f} Å³")

# Convert 10 GPa to eV/Å³ (1 eV/Å³ ≈ 160.218 GPa)
target_pressure = 10 / 160.218

# Initialize thermal velocities at 500K, remove center-of-mass drift
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Run 100-step NPT MD with NPTBerendsen ensemble
dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=500,
    pressure=target_pressure
)
dyn.run(100)

# Record final volume
print(f"Final volume: {atoms.get_volume():.4f} Å³")
