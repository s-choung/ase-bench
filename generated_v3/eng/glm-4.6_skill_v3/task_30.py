from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.615) * (3, 3, 3)
atoms.calc = EMT()

print(f"Initial volume: {atoms.get_volume():.3f} Å³")
print(f"Initial pressure: {atoms.get_pressure():.3f} bar")

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=300, pressure=1.0*units.bar,
                   taut=100*units.fs, taup=1000*units.fs, trajectory='npt.traj')
dyn.run(200)

print(f"Final volume: {atoms.get_volume():.3f} Å³")
print(f"Final pressure: {atoms.get_pressure():.3f} bar")
