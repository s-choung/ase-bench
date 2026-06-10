from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import Atoms

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.01 / units.fs)

def print_temperature(a=atoms):
    print(f"Temperature: {a.get_temperature():.2f} K")

dyn.attach(print_temperature, interval=50)

for step in range(1, 201):
    dyn.run(1)
    if step % 50 == 0:
        target_temp = 300 + (step / 200) * (600 - 300)  # Linearly ramp from 300K to 600K
        dyn.set_temperature(target_temp)
