from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

# Build Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05, cubic=True)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

# Convert 10 GPa to eV/Å³  (1 GPa = 1e9 Pa; 1 eV/Å³ ≈ 160.217 GPa)
pressure_au = 10.0 * units.GPa / (units.eV / units.Å**3)

initial_vol = atoms.get_volume()
print(f"Initial cell volume: {initial_vol:.4f} Å³")

# NPT MD at 500 K, 10 GPa
dyn = NPTBerendsen(
    atoms,
    timestep=1.0 * units.fs,
    temperature_K=500,
    pressure_au=pressure_au,
    compressibility=4.57e-5 / units.bar,
)
dyn.run(steps=100)

final_vol = atoms.get_volume()
print(f"Final cell volume:   {final_vol:.4f} Å³")
