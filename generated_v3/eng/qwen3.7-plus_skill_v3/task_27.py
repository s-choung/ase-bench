from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Ag', 'fcc', a=4.0) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

md = Bussi(atoms, timestep=5*units.fs, temperature_K=500, ttime=50*units.fs)

for _ in range(4):
    md.run(50)
    print(f"Step {md.nsteps:<4} Temperature: {atoms.get_temperature():.2f} K")
