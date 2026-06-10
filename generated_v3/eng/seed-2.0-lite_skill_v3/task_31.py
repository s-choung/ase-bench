from ase.build import bulk
from ase.calculators.emt import EMT
from ase import units
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Build 2x2x2 FCC Al supercell
al_bulk = bulk('Al', 'fcc', a=4.05)
atoms = al_bulk * (2, 2, 2)

# Set built-in EMT calculator
atoms.calc = EMT()

# Convert 10 GPa to ASE's internal eV/Å³ units
pressure = 10 * units.GPa

# Initialize velocities for 500K, remove center-of-mass drift
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Set up NPT Berendsen dynamics
dyn = NPTBerendsen(
    atoms,
    timestep=1 * units.fs,
    temperature_K=500,
    pressure=pressure,
    taut=50 * units.fs,  # Temperature coupling time
    taup=100 * units.fs  # Pressure coupling time
)

# Print initial volume
initial_vol = atoms.get_volume()
print(f"Initial cell volume: {initial_vol:.2f} Å³")

# Run 100 steps of NPT MD
dyn.run(100)

# Print final volume
final_vol = atoms.get_volume()
print(f"Final cell volume: {final_vol:.2f} Å³")
