from ase import units
from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
from ase.calculators.emt import EMT

# Convert pressure from GPa to eV/Ang^3
pressure_GPa = 10.0
pressure_eV_Ang3 = pressure_GPa * units.GPa / (units.J / units.e) * (units.m ** 3) / (units.Ang ** 3)

# Create 2x2x2 Al FCC supercell
atoms = bulk('Al', 'fcc', cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

# Initial volume
initial_volume = atoms.get_volume()

# NPT MD setup
dyn = NPTBerendsen(atoms, timestep=5 * units.fs, temperature_K=500, 
                   taut=0.1 * units.fs, pressure_au=pressure_eV_Ang3, taup=1.0 * units.fs)

# Run MD for 100 steps
dyn.run(100)

# Final volume
final_volume = atoms.get_volume()

# Print initial and final volumes
print(f"Initial volume: {initial_volume:.3f} Ang^3")
print(f"Final volume: {final_volume:.3f} Ang^3")
