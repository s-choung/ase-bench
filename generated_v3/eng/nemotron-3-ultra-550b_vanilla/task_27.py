from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)

dyn = Bussi(atoms, 5 * units.fs, temperature_K=500, taut=100 * units.fs)

def print_temp():
    print(f"Step {dyn.nsteps}: T = {atoms.get_temperature():.2f} K")

dyn.attach(print_temp, interval=50)
dyn.run(200)
