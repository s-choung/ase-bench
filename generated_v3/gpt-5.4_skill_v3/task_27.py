from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)
ZeroRotation(atoms)

dyn = Bussi(atoms, timestep=5 * units.fs, temperature_K=500)

def log_temp():
    print(f"step={dyn.nsteps:4d} T={atoms.get_temperature():.2f} K")

log_temp()
dyn.attach(log_temp, interval=50)
dyn.run(200)
