from ase.lattice.cubic import FaceCenteredCubic
from ase.units import fs, bar, GPa
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md import NPTBerendsen
import numpy as np

# Create 3x3x3 Cu FCC supercell
atoms = FaceCenteredCubic(
    symbol='Cu',
    size=(3, 3, 3),
    pbc=True
)

# Setup calculator and dynamics
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# NPT parameters
timestep = 5 * fs
taut = 100 * fs  # thermostat time constant
taup = 1000 * fs  # barostat time constant
pressure = 1 * bar  # target pressure

# Initial state
initial_volume = atoms.get_volume()
initial_pressure = atoms.get_stress(virial=True).sum() / 3 / GPa  # Convert to GPa for print

# Setup NPTBerendsen dynamics
dyn = NPTBerendsen(
    atoms,
    timestep=timestep,
    temperature_K=300,
    taut=taut,
    pressure_au=pressure / GPa,  # Convert from GPa to ASE internal units (eV/Å^3)
    taup=taup,
    compressibility_au=4.6e-11 / bar  # Cu compressibility
)

# Run 200 steps
dyn.run(200)

# Final state
final_volume = atoms.get_volume()
final_pressure = atoms.get_stress(virial=True).sum() / 3 / GPa

print(f"Initial volume: {initial_volume:.2f} Å³")
print(f"Final volume: {final_volume:.2f} Å³")
print(f"Initial pressure: {initial_pressure:.2f} GPa")
print(f"Final pressure: {final_pressure:.2f} GPa")
