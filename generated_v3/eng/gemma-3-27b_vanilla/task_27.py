from ase.build import fcc111
from ase.md.velocitydistribution import VelocityDistribution
from ase.md.verlet import VelocityVerlet
from ase.thermostats import Bussi
import numpy as np

atoms = fcc111('Ag', size=(2, 2, 2), vacuum=1.0)

dyn = VelocityVerlet(atoms, 5 * 1e-15, thermostat=Bussi(0.5, 500), trajectory='Ag_NVT.traj')
vd = VelocityDistribution(atoms, 500)
vd.set_velocities(atoms)

for step in range(200):
    dyn.run(1)
    if (step + 1) % 50 == 0:
        print(f"Step {step + 1}: Temperature = {atoms.get_temperature():.2f} K")
