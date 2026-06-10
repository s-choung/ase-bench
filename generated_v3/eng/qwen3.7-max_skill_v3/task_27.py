from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Ag', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

def print_temp():
    print(f"Step {md.nsteps:3d}: T = {atoms.get_temperature():.2f} K")

md = Bussi(atoms, timestep=5 * units.fs, temperature_K=500, ttime=100 * units.fs)

print_temp()
md.attach(print_temp, interval=50)
md.run(200)
