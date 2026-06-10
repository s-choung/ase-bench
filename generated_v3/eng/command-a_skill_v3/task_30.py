from ase import units
from ase.build import bulk, make_supercell
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.io import write

# Create 3x3x3 Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.6)
atoms = make_supercell(atoms, (3, 3, 3))

# Set calculator
atoms.calc = EMT()

# Initial volume and pressure
initial_volume = atoms.get_volume()
initial_pressure = atoms.get_stress().mean() * units.bar

# NPT MD setup
dyn = NPTBerendsen(atoms, timestep=5*units.fs, 
                   temperature_K=300, externalstress=1*units.bar,
                   taut=100*units.fs, taup=1000*units.fs)

# Run MD for 200 steps
dyn.run(200)

# Final volume and pressure
final_volume = atoms.get_volume()
final_pressure = atoms.get_stress().mean() * units.bar

# Print results
print(f"Initial Volume: {initial_volume:.2f} Å³, Pressure: {initial_pressure:.2f} bar")
print(f"Final Volume: {final_volume:.2f} Å³, Pressure: {final_pressure:.2f} bar")

# Save final configuration
write('final_config.traj', atoms)
