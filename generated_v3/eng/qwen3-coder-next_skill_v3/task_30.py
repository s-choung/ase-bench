from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create 3x3x3 Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.61) * (3, 3, 3)
atoms.calc = EMT()

# Set initial temperature and pressure
temperature = 300
pressure = 1 * units.bar

# Set initial velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=temperature)
Stationary(atoms)

# NPT Berendsen ensemble
taut = 100 * units.fs
taup = 1000 * units.fs
timestep = 5 * units.fs
nsteps = 200

md = NPTBerendsen(
    atoms,
    timestep=timestep,
    temperature_K=temperature,
    pressure=pressure,
    taut=taut,
    taup=taup,
    trajectory='nptCu.traj'
)

# Print initial cell volume and pressure
initial_vol = atoms.get_volume()
initial_pressure = atoms.get_pressure()
print(f"Initial volume: {initial_vol:.3f} Å³")
print(f"Initial pressure: {initial_pressure:.3f} bar")

# Run MD
md.run(nsteps)

# Print final cell volume and pressure
final_vol = atoms.get_volume()
final_pressure = atoms.get_pressure()
print(f"Final volume: {final_vol:.3f} Å³")
print(f"Final pressure: {final_pressure:.3f} bar")
