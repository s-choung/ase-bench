from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Ag', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

dyn = Bussi(atoms, timestep=5 * units.fs, temperature_K=500, taut=100 * units.fs)

def log():
    print(f"Step {dyn.nsteps:4d}  T = {atoms.get_temperature():.2f} K")

dyn.attach(log, interval=50)
log()
dyn.run(200)
