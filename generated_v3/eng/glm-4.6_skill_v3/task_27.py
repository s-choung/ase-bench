from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

dyn = Bussi(atoms, timestep=5*units.fs, temperature_K=500, taut=100*units.fs)

def print_temperature():
    if dyn.get_number_of_steps() % 50 == 0:
        print(f"Step {dyn.get_number_of_steps()}: T = {atoms.get_temperature():.1f} K")

dyn.attach(print_temperature, interval=1)
dyn.run(200)
