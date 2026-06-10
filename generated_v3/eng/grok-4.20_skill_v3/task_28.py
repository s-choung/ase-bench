from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

md = Langevin(atoms, timestep=5 * units.fs, temperature_K=300,
              friction=0.01 / units.fs, trajectory='cu.traj')

def print_temp(a=atoms):
    print(f"T = {a.get_temperature():.1f} K")

md.attach(print_temp, interval=50)
md.run(200)
