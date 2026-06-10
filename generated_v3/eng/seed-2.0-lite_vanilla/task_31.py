from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
import ase.units as units

# Create Al FCC 2x2x2 supercell
al_atoms = bulk('Al', 'fcc', a=4.05).repeat((2, 2, 2))
al_atoms.calc = EMT()

# Unit conversion: 10 GPa to eV/Å³ (1 eV/Å³ ≈ 160.22 GPa)
pressure_evA3 = 10 / 160.2176634

# Get initial volume
initial_vol = al_atoms.get_volume()
print(f"Initial cell volume: {initial_vol:.2f} Å³")

# Set up NPT Berendsen dynamics
dyn = NPTBerendsen(
    al_atoms,
    timestep=1 * units.fs,
    temperature_K=500,
    pressure=pressure_evA3,
    taup=100 * units.fs,
    ttime=50 * units.fs
)

# Run 100 MD steps
dyn.run(100)

# Get final volume
final_vol = al_atoms.get_volume()
print(f"Final cell volume: {final_vol:.2f} Å³")
