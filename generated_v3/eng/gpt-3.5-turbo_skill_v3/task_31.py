from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.units import GPa, eV, Ang, fs

# Create an aluminum FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05)*2

# Set EMT calculator
atoms.calc = EMT()

# Define the target temperature and pressure
temperature = 500  # K
pressure = 10*GPa  # Pressure in GPa

# Create NPTBerendsen MD object
dyn = NPTBerendsen(atoms, timestep=5*fs, temperature_K=temperature, pressure_GPa=pressure,
                   taut=100*fs, taut_eta=100*fs)  # taut: thermostat time constant, taut_eta: barostat time constant

# Run MD for 100 steps
dyn.run(100)

# Convert pressure from GPa to eV/Ang^3
pressure_eV_Ang3 = pressure*eV/(Ang**3)

# Print initial/final cell volume
initial_volume = atoms.get_volume()
final_volume = dyn.atoms.get_volume()

print(f"Initial Cell Volume: {initial_volume:.3f} Ang^3")
print(f"Final Cell Volume: {final_volume:.3f} Ang^3")
