from ase.build import bulk
from ase.md.npt import NPTBerendsen
from ase.calculators.emt import EMT
from ase import units

# Constants
temperature = 500  # Kelvin
pressure_GPa = 10  # GPa
pressure_eVA3 = pressure_GPa / 160.21766208  # GPa to eV/Ang^3 conversion
steps = 100
timestep = 1  # fs

# Create aluminum FCC 2x2x2 supercell
aluminum = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
aluminum.set_calculator(EMT())

# Set up NPTBerendsen
dyn = NPTBerendsen(aluminum, timestep * units.fs, 
                   temperature_K=temperature, 
                   pressure=pressure_eVA3, 
                   taut=0.5 * 1000 * units.fs, 
                   taup=0.5 * 1000 * units.fs)

# Record initial volume
initial_volume = aluminum.get_volume()
print(f"Initial volume: {initial_volume:.3f} Å^3")

# Run MD
dyn.run(steps)

# Record final volume
final_volume = aluminum.get_volume()
print(f"Final volume: {final_volume:.3f} Å^3")
