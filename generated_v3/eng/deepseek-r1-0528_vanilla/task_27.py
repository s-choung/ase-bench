from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import Langevin
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = bulk('Ag', 'fcc', a=4.09).repeat((2, 2, 2))
atoms.calc = EMT()
temperature = 500
timestep = 5 * units.fs
MaxwellBoltzmannDistribution(atoms, temperature_K=temperature)
dyn = Langevin(atoms, timestep, temperature * units.kB, 0.01)

def print_temp():
    step = dyn.get_number_of_steps()
    if step % 50 == 0:
        print(f"Step {step}: Temperature = {atoms.get_temperature():.2f} K")

dyn.attach(print_temp, interval=1)
dyn.run(200)
