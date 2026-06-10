from ase.build import bulk
from ase.calculators.emt import EMT
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.nptberendsen import NPTBerendsen

# Build 3x3x3 Cu fcc supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((3, 3, 3))
atoms.calc = EMT()

# Calculate and print initial state
initial_vol = atoms.get_volume()
initial_press = atoms.get_pressure() / units.bar  # Convert to bar
print(f"Initial: Volume = {initial_vol:.2f} Å³, Pressure = {initial_press:.2f} bar")

# Initialize velocities and remove COM drift
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Set up NPT Berendsen dynamics
dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure=1 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs
)

# Run 200 MD steps
dyn.run(200)

# Calculate and print final state
final_vol = atoms.get_volume()
final_press = atoms.get_pressure() / units.bar
print(f"Final:   Volume = {final_vol:.2f} Å³, Pressure = {final_press:.2f} bar")
