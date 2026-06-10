from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.nptberendsen import NPTBerendsen
from ase import units

# Create 2x2x2 FCC Al supercell
atoms = bulk('Al', crystalstructure='fcc', a=4.05)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

# Initial volume
vol0 = atoms.get_volume()
print(f"Initial volume: {vol0:.2f} Å³")

# Convert pressure: 10 GPa to eV/Å³
pressure_eV_per_A3 = 10e9 * units.Pascal / (units.eV / units.Ang**3)

# Setup NPT MD with NPTBerendsen
dyn = NPTBerendsen(
    atoms,
    timestep=1.0 * units.fs,
    temperature_K=500,
    pressure_au=pressure_eV_per_A3,
    taut=1000 * units.fs,
    taup=1000 * units.fs,
)

# Run 100 steps
dyn.run(100)

# Final volume
vol_final = atoms.get_volume()
print(f"Final volume: {vol_final:.2f} Å³")
