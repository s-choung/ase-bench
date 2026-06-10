from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
import ase.units as units

atoms = bulk('Ag', 'fcc', a=4.09, size=(2, 2, 2))
atoms.set_calculator(EMT())
atoms.set_initial_velocities(temperature=500)

dt = 5 * units.fs
dyn = VelocityVerlet(atoms, dt, thermostat='Bussi', temperature=500)

for step in range(200):
    dyn.run(1)
    if step % 50 == 0:
        print(f"Step {step}: {atoms.get_temperature()} K")
