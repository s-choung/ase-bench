from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create 3x3x3 supercell of Cu FCC
atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms.repeat((3, 3, 3))
atoms.calc = EMT()

# Initialize velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Print initial state
print(f"Initial volume: {atoms.get_volume():.2f} Å³")
stress = atoms.get_stress()
pressure = -(stress[0] + stress[1] + stress[2]) / 3 / units.bar
print(f"Initial pressure: {pressure:.2f} bar")

# Set up NPT MD
md = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure_au=1.0 / units.bar,  # 1 bar in atomic units
    taut=100 * units.fs,
    taup=1000 * units.fs
)

# Run MD
md.run(200)

# Print final state
print(f"Final volume: {atoms.get_volume():.2f} Å³")
stress = atoms.get_stress()
pressure = -(stress[0] + stress[1] + stress[2]) / 3 / units.bar
print(f"Final pressure: {pressure:.2f} bar")
