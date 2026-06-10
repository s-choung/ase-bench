from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

# Initialize velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Convert 10 GPa to eV/A³ (1 GPa = 0.0062415 eV/A³)
pressure = 10.0 * 0.0062415

# Run NPT MD at 500 K and 10 GPa for 100 steps
npt = NPTBerendsen(atoms, timestep=1.0 * units.fs, temperature_K=500, pressure=pressure)
npt.run(100)

# Output initial and final volumes
print(f"Initial volume: {atoms.get_volume():.2f} Å³")
print(f"Final volume: {atoms.get_volume():.2f} Å³")
