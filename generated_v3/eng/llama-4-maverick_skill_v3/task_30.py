from ase import Atoms, units
from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
from ase.calculators.emt import EMT
from ase.io import write

# Set up Cu FCC 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

# Print initial cell volume and pressure
initial_volume = atoms.get_volume()
initial_pressure = atoms.get_stress().diag.mean() * -units.GPa  # Convert to bar (1 GPa = 10 kbar)
print(f"Initial volume: {initial_volume:.2f} Å³, Initial pressure: {initial_pressure:.2f} bar")

# NPT MD using NPTBerendsen
dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=300, pressure_bar=1.0,
                   taut=100*units.fs, taup=1000*units.fs)
dyn.run(200)

# Print final cell volume and pressure
final_volume = atoms.get_volume()
final_pressure = atoms.get_stress().diag.mean() * -units.GPa  # Convert to bar
print(f"Final volume: {final_volume:.2f} Å³, Final pressure: {final_pressure:.2f} bar")

# Save final configuration
write('final_npt.xyz', atoms)
