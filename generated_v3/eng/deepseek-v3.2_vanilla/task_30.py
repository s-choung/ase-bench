from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.md.npt import NPTBerendsen
from ase.io import Trajectory
import numpy as np

# Create FCC Cu supercell
atoms = Atoms('Cu', positions=[[0, 0, 0]], cell=3.61 * np.ones(3), pbc=True)
atoms = atoms.repeat((3, 3, 3))
atoms.calc = EMT()

# Define parameters
dt = 5 * units.fs
taut = 100 * units.fs
taup = 1000 * units.fs
temperature = 300.0
pressure = 1.01325  # bar
steps = 200

# Initial values
initial_volume = atoms.get_volume()
initial_stress = atoms.get_stress() / units.GPa
initial_pressure = -np.mean(initial_stress[:3])

print(f'Initial: volume = {initial_volume:.2f} Å³, pressure = {initial_pressure:.3f} GPa')

# Setup NPT MD
dyn = NPTBerendsen(atoms, timestep=dt, temperature_K=temperature,
                   pressure_au=pressure * units.bar, taut=taut, taup=taup,
                   trajectory='npt_cu.traj')

# Run MD
dyn.run(steps)

# Final values
final_volume = atoms.get_volume()
final_stress = atoms.get_stress() / units.GPa
final_pressure = -np.mean(final_stress[:3])

print(f'Final: volume = {final_volume:.2f} Å³, pressure = {final_pressure:.3f} GPa')
