from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09).repeat([2, 2, 2])
atoms.calc = EMT()

from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

dyn = Bussi(atoms, timestep=5 * units.fs, temperature_K=500, taut=100 * units.fs)

print(f"{'Step':>6}  {'Temperature (K)':>16}")
print("-" * 26)

def print_temp():
    step = dyn.get_number_of_steps()
    temp = atoms.get_temperature()
    print(f"{step:>6}  {temp:>16.2f}")

dyn.attach(print_temp, interval=50)
print_temp()
dyn.run(200)
