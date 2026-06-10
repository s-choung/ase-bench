from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import neighborlist

# Create a Cu FCC 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms.repeat((3, 3, 3))

# Set the calculator to EMT
atoms.calc = EMT()

# Print initial cell and volume
initial_volume = atoms.get_volume()
initial_cell = atoms.get_cell_lengths_and_angles()
print(f"Initial cell: {initial_cell[:3]}")
print(f"Initial volume: {initial_volume:.2f} Å^3")

# Set the initial temperature, target pressure, and barostat/damper parameters
temperature = 300  # in Kelvin
target_pressure = 1  # in bar
tau_t = 100 * units.fs
tau_p = 1000 * units.fs

# Set up the MD with NPTBerendsen thermostat and barostat
dyn = NPTBerendsen(atoms,
                   timestep=5 * units.fs,
                   temperature=temperature * units.kB,
                   externalstress=1.0 * units.GPa,
                   taup=tau_p,
                   tau_t=tau_t)

# Run the MD for 200 steps
dyn.run(200)

# Print final cell and volume
final_volume = atoms.get_volume()
final_cell = atoms.get_cell_lengths_and_angles()
print(f"Final cell: {final_cell[:3]}")
print(f"Final volume: {final_volume:.2f} Å^3")

# Output the final pressure
final_pressure = dyn.get_stress()[0] * units.GPa  # Convert from GPa to bar
print(f"Final pressure: {final_pressure / units.bar:.2f} bar")
