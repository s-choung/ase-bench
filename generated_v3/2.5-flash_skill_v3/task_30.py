from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io.trajectory import Trajectory

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)
atoms = atoms.repeat((3, 3, 3))

atoms.calc = EMT()

initial_volume = atoms.get_volume()
print(f"Initial cell volume: {initial_volume:.2f} Å³")

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

timestep = 5 * units.fs
temperature_K = 300
external_pressure = 1 * units.bar # Target pressure
taut = 100 * units.fs
taup = 1000 * units.fs

md = NPTBerendsen(atoms,
                  timestep=timestep,
                  temperature_K=temperature_K,
                  externalstress=-external_pressure, # Negative for external pressure
                  taut=taut,
                  taup=taup,
                  trajectory='npt_cu.traj',
                  logfile='npt_cu.log')

md.run(200)

final_volume = atoms.get_volume()
final_pressure = atoms.get_pressure()

print(f"Final cell volume: {final_volume:.2f} Å³")
print(f"Final pressure: {final_pressure / units.bar:.2f} bar")
