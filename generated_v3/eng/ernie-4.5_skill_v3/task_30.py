from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create Cu FCC 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((3, 3, 3))
atoms.calc = EMT()

# Set initial velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Print initial volume and pressure (pressure requires calculator support)
print(f"Initial volume: {atoms.get_volume():.2f} Å³")
# Note: EMT doesn't calculate pressure, so we'll get None. In real use, consider a calculator that does (e.g., LAMMPS, DFT)
# For demonstration, we'll just print None for initial pressure
print(f"Initial pressure: {atoms.get_pressure() if hasattr(atoms, 'get_pressure') else 'N/A (EMT not supported)'}") 
# Alternatively, if pressure calculation is critical, consider using a different calculator

# Setup and run NPT MD
md = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    taut=100 * units.fs,
    pressure_Pa=1 * units.bar,  # 1 bar in Pa
    taup=1000 * units.fs,
    compressibility_Pa=None  # Optional, if not set automatically determined for solids
)

def print_status():
    vol = atoms.get_volume()
    pres = atoms.get_pressure() if hasattr(atoms, 'get_pressure') else None
    print(f"Volume: {vol:.2f} Å³, Pressure: {pres if pres is not None else 'N/A'} Pa")

print("Before MD:")
print_status()

md.run(200)

print("After MD:")
print_status()
