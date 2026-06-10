from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen

# Create Al FCC 2xx2 supercell
atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

# Convert 10 GPa to eV/Å³: 1 GPa = 1e9 Pa = 1e9 J/m³ = 1e9 * (1e-10)^3 J/Å³ = 1e-21 J/Å³
# 1 eV = 1.602176634e-19 J → 1 GPa = 1e-21 / 1.602176634e-19 = ~0.00624 eV/Å³
pressure_gpa = 10.0
pressure_eva3 = pressure_gpa * 1e9 * 1e-30 / units.J * units.eV  # Pa * m³ → J → eV

# Initial volume
initial_volume = atoms.get_volume()

# Set up NPT Berendsen
dyn = NPTBerendsen(atoms, timestep=2*units.fs, temperature_K=500,
                   pressure_au=pressure_eva3, ttime=100*units.fs, pfactor=1e-3)

# Run MD for 100 steps
dyn.run(100)

# Final volume
final_volume = atoms.get_volume()

print(f"Initial volume: {initial_volume:.3f} Å³")
print(f"Final volume: {final_volume:.3f} Å³")
