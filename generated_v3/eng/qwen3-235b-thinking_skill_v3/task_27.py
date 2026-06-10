from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Ag') * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, 500)
Stationary(atoms)

print(f"Step 0: Temperature = {atoms.get_temperature():.2f} K")
md = Bussi(atoms, 5 * units.fs, temperature_K=500)

def print_temp():
    step = md.nsteps
    temp = atoms.get_temperature()
    print(f"Step {step}: Temperature = {temp:.2f} K")

md.attach(print_temp, interval=50)
md.run(200)
