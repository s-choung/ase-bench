from ase.build import bulk
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01 / units.fs)

def print_temp():
    step = dyn.get_number_of_steps()
    if step % 50 == 0:
        temp = atoms.get_temperature()
        print(f"Step {step}: Temperature = {temp:.1f} K")

dyn.attach(print_temp)

for step in range(200):
    target_temp = 300 + (600 - 300) * step / 200
    dyn.set_temperature(temperature_K=target_temp)
    dyn.run(1)
