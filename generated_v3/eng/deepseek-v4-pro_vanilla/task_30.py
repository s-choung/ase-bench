import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.units import fs, GPa
from ase.md.nptberendsen import NPTBerendsen
from ase.io.trajectory import Trajectory

# Build Cu FCC 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

# Initialise velocities at 300 K
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
MaxwellBoltzmannDistribution(atoms, temperature_K=300 * atoms.get_number_of_atoms())

# Save initial volume and pressure
initial_volume = atoms.get_volume()
stress = atoms.get_stress()
initial_pressure_GPa = -np.trace(stress[:3]) / 3.0
initial_pressure_bar = initial_pressure_GPa * 1e4

# Setup NPTBerendsen dynamics
dyn = NPTBerendsen(
    atoms,
    timestep=5 * fs,
    temperature_K=300,
    externalstress=1e5,  # 1 bar in Pa
    taut=100 * fs,
    taup=1000 * fs,
)

# Run for 200 steps (no trajectory output needed)
dyn.run(200)

# Final volume and pressure
final_volume = atoms.get_volume()
stress = atoms.get_stress()
final_pressure_GPa = -np.trace(stress[:3]) / 3.0
final_pressure_bar = final_pressure_GPa * 1e4

print(f"Initial volume: {initial_volume:.3f} Å³, pressure: {initial_pressure_bar:.3f} bar")
print(f"Final volume:   {final_volume:.3f} Å³, pressure: {final_pressure_bar:.3f} bar")
