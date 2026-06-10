from ase.build import bulk
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Ag', 'fcc', a=4.08).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

dyn = Bussi(atoms, timestep=5 * units.fs, temperature_K=500, taut=0.1 / units.fs)

def print_temp():
    print(f"Step {dyn.get_number_of_steps()}: T = {atoms.get_temperature():.1f} K")

for i in range(200):
    dyn.run(1)
    if (i + 1) % 50 == 0:
        print_temp()
