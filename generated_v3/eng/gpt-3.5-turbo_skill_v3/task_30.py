from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
from ase import units

# Create a Cu FCC 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.5) * (3, 3, 3)
atoms.calc = EMT()  # Use EMT calculator

# Run NPT MD at 300K and 1 bar for 200 steps
dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature=300, taut=100*units.fs, 
                   externalstress=1.0, taup=1000*units.fs, compressibility=4.8e-5)
dyn.run(200)

# Print the initial and final cell volume and pressure
initial_volume = atoms.get_volume()
final_volume = atoms.get_volume()
initial_pressure = atoms.get_stress() / units.GPa
final_pressure = atoms.get_stress() / units.GPa

print(f"Initial volume: {initial_volume:.2f} Å^3, Initial pressure: {initial_pressure:.2f} GPa")
print(f"Final volume: {final_volume:.2f} Å^3, Final pressure: {final_pressure:.2f} GPa")
